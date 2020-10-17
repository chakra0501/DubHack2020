from flask import Flask, url_for, send_file, make_response, request, jsonify
import UserStore

usernameDict = {}

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

    #Different Users
    newUser = UserStore(username, gender, loc, workout_type, age, about, email)
    usernameDict[username] = newUser
    
    #Workout Types
    if workout_type in workoutDict:
        workoutDict[workout_type].append(username)
    else:
        workoutDict[workout_type] = [username]
    
@app.route('/newLike')
def newLike():
    oldUser, newLike = request.args.get('olduser'), request.args.get('newlike')
    usernameDict[oldUser].addLike(newLike)
    
@app.route('/getLike')
def getLike():
    oldUser = request.args.get('olduser')
    if oldUser in usernameDict:
        return jsonify(results=usernameDict[oldUser].getLikes())
    return "N/A"
    
@app.route('/removeLike')
def removeLike():
    oldUser, newLike = "joy", "person"
    usernameDict[oldUser].removeLike(newLike)

# 127.0.0.1/8080/matches?username=bob

@app.route('/getMatch')
def getMatches():
    name = request.args.get('username')
    if request.args.get('username') in usernameDict:
        return jsonify(results=usernameDict[name].getMatches())
    return "N/A"
        


    
    
    

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