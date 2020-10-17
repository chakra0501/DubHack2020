
class User:
    def __init__(self, username, 
                    gender : str, 
                    loc : str, 
                    workout_type : str, 
                    age : int,
                    about : str,
                    email : str):
        self.gender = gender 
        self.location = loc #City
        self.workout_type = workout_type
        self.age = age 
        self.username = username 
        self.about = about 
        self.email = email
        
        #Likes
        self.likes = set()
        
        #Matches
        self.match = set()

    #Get Info
    def getInfo(self):
        out = {
            'username' : self.username,
            'gender' : self.gender,
            'loc' : self.location,
            'workout' : self.workout_type,
            'about' : self.about,
            'email' : self.email,
            'age' : self.age 
        }
        return out
    
    #Changing Likes
    def addLike(self, username):
        self.likes.add(username)

    def getLikes(self):
        return self.likes
        
    def removeLike(self, username):
        if username in self.likes:
            self.likes.remove(username)
    
    #Changing Matches
    def addMatch(self, username):
        self.match.add(username)
        
    def getMatches(self):
        return self.match

    def removeMatch(self, username):
        if username in self.match:
            self.match.remove(username)
            
    #Update Info
    def updateInfo(self, 
                    gender = None, 
                    loc = None, 
                    workout_type = None, 
                    age = None,
                    about = None,
                    email = None):
        if(gender):
            self.gender = gender 
        if(loc):
            self.location = loc #City
        if(workout_type):
            self.workout_type = workout_type
        if(age):
            self.age = age 
        if(about):
            self.about = about 
        if(email):
            self.email = email
        
    
        

        




