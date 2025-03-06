class Task:
    def __init__(self,name,priority ="Media",state = "Abierta"):
        self.__name = name
        self.__priority = priority
        self.__state = state
    
    def getName(self):
        return self.__name
    def getPriority(self):
        return self.__priority
    def getState(self):
        return self.__state
    
    def changeName(self,name):
        self.__name = name

    def changePriority(self,priority):
        self.__priority = priority

    def completeTask(self):
        self.__state = "Cerrada"

    def __str__(self):
        return f'{self.__state}---{self.__name}---{self.__priority}'