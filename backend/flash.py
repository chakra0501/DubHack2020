#!/usr/bin/env python3
from flask import Flask, url_for, send_file, make_response, request, jsonify
from flask_cors import CORS
import UserStore

#Test Addition to the Dictionary
bob = UserStore.User("bob","male","Seattle","Abs",23,"I'm buff","bob101@gmail.com", 'Bob', 'Marley')
joy = UserStore.User("joy", "female", "Chicago", "Abs", 23, "Poojan GF", "poojanGF@poojangf.com", 'Joy', 'Mun')
julio = UserStore.User("julio","female", "Los Angeles", "Abs", 40, "hello world", "hi@email", "Julio", "Jones")
julio.addLike('bob')
julio.addLike('joy')

#The Two Main Dictionaries to be Used
usernameDict = {'bob' : bob, 'joy' : joy, 'julio' : julio}
#usernameDict = {}
workoutDict = {'Abs' : ['bob','joy']}

for i in range(100):
    key = 'bob'+str(i) 
    val = UserStore.User("bob"+str(i),"male","Seattle","Abs",23,"I'm buff","bob101@gmail.com", 'Bob'+str(i), 'Marley')
    print("hello!")
    usernameDict[key] = val
    if val.workout_type in workoutDict:
        workoutDict[val.workout_type].append(key)
    else:
        workoutDict[val.workout_type] = [key]
for (k, v) in usernameDict.items():
    v.updatePotential(workoutDict[v.getWorkout()])

#Main Flask name
app = Flask(__name__)
CORS(app)

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
@app.route('/getNext', methods=['POST']) 
def getNext():
    username = request.args.get('user')
    curr = usernameDict[username].getNextPotential()
    print(curr)
    return usernameDict[curr].getInfo()

#Updating all Potential Matches with New Users with Same Workout Type
@app.route('/updatePotential', methods=['POST'])
def updatePotential():
    username = request.args.get('user')
    curr = usernameDict[username]
    curr.updatePotential(workoutDict[curr.getWorkout()])
    return "success"

#Moving a Potential Match to the Back Due to Dislike (Swipe Left)
@app.route('/newDislike', methods=['POST'])
def newDislike():
    oldUser, newDislike = request.args.get('user'), request.args.get('like')
    curr = usernameDict[oldUser]
    curr.AddPotentialToEnd(newDislike)
    return "success"
    
#Moving a potential match to likes (Swipe Right)
@app.route('/newLike', methods=['POST'])
def newLike():
    oldUser, newLike = request.args.get('user'), request.args.get('like')
    print(newLike)
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
@app.route('/getLike', methods=['POST'])
def getLike():
    oldUser = request.args.get('user')
    print(usernameDict)
    print(oldUser)
    if oldUser in usernameDict:
        return jsonify(results=list(usernameDict[oldUser].getLikes()))
    return "N/A"

#Getting Info On The User
@app.route('/infoUser', methods=['POST'])
def infoUser():
    if request.json:
        print('Got JSON!')
    infoUser = request.args.get('user')
    print(usernameDict)
    print(infoUser)
    if infoUser in usernameDict:
        print("Successful!")
        print(usernameDict[infoUser].getInfo())
        return jsonify(usernameDict[infoUser].getInfo())
    print("Data not available...")
    return jsonify({'username' : None})

#User can remove a particular like    
@app.route('/removeLike', methods=['POST'])
def removeLike():
    oldUser, newLike = request.args.get('user'), request.args.get('like')
    usernameDict[oldUser].removeLike(newLike)
    return "success"

#Get All Of The Current Matches
@app.route('/getMatch', methods=['POST'])
def getMatches():
    name = request.args.get('user')
    if name in usernameDict:
        return jsonify(results=list(usernameDict[name].getMatches()))
    return "N/A"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 3000, debug = True)
    
#Sample Urls
#127.0.0.1/8080/matches?username=bob
