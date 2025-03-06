from user import User
import json

class UserGestor:
    def __init__(self):
        self.__users:list[User] = []
    
    def addUser(self,name,age,email):
        user = User(name,age,email)
        self.__users.append(user)
    
    def searchUser(self,email):
        for user in self.__users:
            if email == user.getEmail():
                print(user)
    
    def removeUser(self,email):
        for user in self.__users:
            if email == user.getEmail():
                self.__users.remove(user)
                print(f"Se ha eliminado el usuario con email {user.getEmail()}")
    
    def loadUsers(self,path):
        try:
            with open(path,"r") as file:
                json_users = json.dump(file)
                for user in json_users:
                    self.__users.append(user)
        except:
            open(path,"x")
            

