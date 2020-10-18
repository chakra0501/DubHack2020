import heapq

class User:
    def __init__(self, username, 
                    gender : str, 
                    loc : str, 
                    workout_type : str, 
                    age : int,
                    about : str,
                    email : str,
                    first : str,
                    last : str):
        self.gender = gender 
        self.location = loc #City
        self.workout_type = workout_type
        self.age = age 
        self.username = username 
        self.about = about 
        self.email = email
        self.first = first
        self.last = last
        
        #Likes
        self.likes = set()
        
        #Matches
        self.match = set()
        
        #Potential
        self.potentialCtr = 0
        self.potential = []

    #Get Info
    def getInfo(self):
        out = {
            'username' : self.username,
            'gender' : self.gender,
            'loc' : self.location,
            'workout' : self.workout_type,
            'about' : self.about,
            'email' : self.email,
            'age' : self.age,
            'first': self.first,
            'last': self.last 
        }
        return out
    
    #Return Workout
    def getWorkout(self):
        return self.workout_type
    
    #Changing Likes
    def addLike(self, username):
        print(username)
        self.likes.add(username)

    def getLikes(self):
        return self.likes
        
    def removeLike(self, username):
        if username in self.likes:
            self.likes.remove(username)
    
    #Changing Matches
    def addMatch(self, username):
        self.likes.remove(username)
        self.match.add(username)
        
    def getMatches(self):
        return self.match

    def removeMatch(self, username):
        if username in self.match:
            self.match.remove(username)
            
    #Potential
    def updatePotential(self,workoutList):
        self.potentialCtr = 0
        self.potential = list(set(workoutList) - set(self.potential) - set(self.likes) - set(self.match)) + self.potential
    
    def getNextPotential(self):
        self.potentialCtr += 1
        if(self.potentialCtr == len(self.potential)):
            return None
        return self.potential[0]
    
    def AddPotentialToEnd(self,item):
        self.potential.remove(item)
        self.potential.append(item)
        
    def removePotential(self,item):
        self.potential.remove(item)   
            
    #Update Info
    def updateInfo(self, 
                    gender = None, 
                    loc = None, 
                    workout_type = None, 
                    age = None,
                    about = None,
                    email = None, first = None,
                    last = None):
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
        if (first):
            self.first = first 
        if (last): 
            self.last = last 
        
    
        

        




