#!/usr/bin/env python3
from flask import Flask, url_for, send_file, make_response, request, jsonify
from UserStore import UserStore

"""Test Addition to the Dictionary
bob = UserStore.User("bob","male","Seattle","Abs",23,"I'm buff","bob101@gmail.com", 'Bob', 'Marley')
joy = UserStore.User("joy", "female", "Chicago", "butt", 23, "Poojan GF", "poojanGF@poojangf.com", 'Joy', 'Mun')
julio = UserStore.User("julio","female", "Los Angeles", "chest", 40, "hello world", "hi@email", "Julio", "Jones")
julio.addLike('bob')
julio.addLike('joy')
julio.addMatch('bob')"""


#The Two Main Dictionaries to be Used
#usernameDict = {'bobby' : bob, 'joy' : joy, 'julio' : julio}
usernameDict = {}
workoutDict = {}

#Main Flask name
app = Flask(__name__)

#Calling and Generating a New User
@app.route('/newUser') 
def newUser():
    #All of the Different Parameters
    username = request.args.get('user')
    gender = request.args.get('gender')
    loc = request.args.get('loc')
    workout_type = request.args.get('work')
    age = int(request.args.get('age'))
    about = request.args.get('about')
    email = request.args.get('email')
    first = request.args.get('first')
    last = request.args.get('last')

    #Different Users
    newUser = UserStore.User(username, gender, loc, workout_type, age, about, email, first, last)
    usernameDict[username] = newUser
    
    #Workout Types
    if workout_type in workoutDict:
        workoutDict[workout_type].append(username)
    else:
        workoutDict[workout_type] = [username]
    return "success"

#Getting the Next User to Potentially Match
@app.route('/getNext') 
def getNext():
    username = request.args.get('user')
    curr = usernameDict[username].getNextPotential()
    return curr

#Updating all Potential Matches with New Users with Same Workout Type
@app.route('/updatePotential') 
def updatePotential():
    username = request.args.get('user')
    curr = usernameDict[username]
    curr.updatePotential(workoutDict[curr.getWorkout()])
    return "success"

#Moving a Potential Match to the Back Due to Dislike (Swipe Left)
@app.route('/newDislike')
def newDislike():
    oldUser, newDislike = request.args.get('user'), request.args.get('like')
    curr = usernameDict[oldUser]
    curr.AddPotentialToEnd(newDislike)
    return "success"
    
#Moving a potential match to likes (Swipe Right)
@app.route('/newLike')
def newLike():
    oldUser, newLike = request.args.get('user'), request.args.get('like')
    if newLike in usernameDict:
        #Removes from the Potential matches to Likes
        usernameDict[oldUser].removePotential(newLike)
        
        #Checking if the other user Liked and Adding to matches If Done
        if oldUser in usernameDict[newLike].getLikes():
            usernameDict[newLike].removeLike(oldUser)
            usernameDict[newLike].addMatch(oldUser)
            usernameDict[oldUser].addMatch(newLike)
        else:
            usernameDict[oldUser].addLike(newLike)
            
        #Different Returns to Indicate Success or Failure
        return "success"
    else:
        return "user not found"
    
#Getting all the Current Likes
@app.route('/getLike')
def getLike():
    oldUser = request.args.get('user')
    #print(usernameDict)
    #print(oldUser)
    if oldUser in usernameDict:
        return jsonify(results=list(usernameDict[oldUser].getLikes()))
    return "N/A"

#Getting Info On The User
@app.route('/infoUser')
def infoUser():
    infoUser = request.args.get('user')
    #print(usernameDict)
    #print(infoUser)
    if infoUser in usernameDict:
        return jsonify(usernameDict[infoUser].getInfo())
    return "N/A"

#User can remove a particular like    
@app.route('/removeLike')
def removeLike():
    oldUser, newLike = request.args.get('user'), request.args.get('like')
    usernameDict[oldUser].removeLike(newLike)
    return "success"

#Get All Of The Current Matches
@app.route('/getMatch')
def getMatches():
    name = request.args.get('user')
    if name in usernameDict:
        return jsonify(results=list(usernameDict[name].getMatches()))
    return "N/A"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port = 8080, debug = True)
    
#Sample Urls
#127.0.0.1/8080/matches?username=bob