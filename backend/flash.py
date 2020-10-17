from flask import Flask, url_for, send_file, make_response, request, jsonify
import UserStore

bob = UserStore.User("bob","male","Seattle","Abs",23,"I'm buff","bob101@gmail.com", 'Bob', 'Marley')
joy = UserStore.User("joy", "female", "Chicago", "butt", 23, "Poojan GF", "poojanGF@poojangf.com", 'Joy', 'Mun')
julio = UserStore.User("julio","female", "Los Angeles", "chest", 40, "hello world", "hi@email", "Julio", "Jones")
julio.addLike('bob')
julio.addLike('joy')
julio.addMatch('bob')
usernameDict = {'bobby' : bob, 'joy' : joy, 'julio' : julio}

workoutDict = {}

app = Flask(__name__)

@app.route('/newUser') 
def newUser():
    #All of the Different Parameters
    username = request.args.get('user')
    gender = request.args.get('gender')
    loc = request.args.get('loc')
    workout_type = request.args.get('workout_type')
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
    
@app.route('/newLike')
def newLike():
    oldUser, newLike = request.args.get('oldUser'), request.args.get('newLike')
    print(newLike)
    usernameDict[oldUser].addLike(newLike)
    return "success"
    
@app.route('/getLike')
def getLike():
    oldUser = request.args.get('oldUser')
    print(usernameDict)
    print(oldUser)
    if oldUser in usernameDict:
        return jsonify(results=list(usernameDict[oldUser].getLikes()))
    return "N/A"

@app.route('/infoUser')
def infoUser():
    infoUser = request.args.get('username')
    print(usernameDict)
    print(infoUser)
    if infoUser in usernameDict:
        return jsonify(usernameDict[infoUser].getInfo())
    return "N/A"
    
@app.route('/removeLike')
def removeLike():
    oldUser, newLike = "joy", "person"
    usernameDict[oldUser].removeLike(newLike)
    return "success"

# 127.0.0.1/8080/matches?username=bob

@app.route('/getMatch')
def getMatches():
    name = request.args.get('username')
    if request.args.get('username') in usernameDict:
        return jsonify(results=list(usernameDict[name].getMatches()))
    return "success"
        


    
    
    

"""
@app.route('/image')
def get_image():
    imageFolder = '/Users/jonathanke/Documents/SimpleMosaic/BackEnd/images-moon'
    paths = os.listdir(imageFolder)
    choice = imageFolder+'/'+random.choice(paths)
    return send_file(choice)
"""

if __name__ == "__main__":
    app.run(host='127.0.0.1', port = 8080, debug = True)