class User:
    def __init__(self,name,age,email):
        self.__name = name
        self.__age = age
        self.__email = email
    
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getEmail(self):
        return self.__email
    
    def to_dict(self):
        return {'nombre':self.__name,"edad":self.__age,"email":self.__email}

    def __str__(self):
        print(f'Usuario con nombre {self.__name}, edad de {self.__age} y email {self.__email}')