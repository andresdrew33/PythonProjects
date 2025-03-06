from task import Task

class Gestor:
    def __init__(self):
        self.__tasks:list[Task] = []
    
    def addTask(self,name,priority):
       task = Task(name,priority)
       self.__tasks.append(task)

    def showTasks(self):
        for task in self.__tasks:
            print(task)
    
    def completeTask(self,name):
        for task in self.__tasks:
            if name==task.getName():
                task.completeTask()
                print(f"Se ha cerrado la tarea--> {name}")

    def saveInFile(self):
        with open("tareas.txt","w") as archivo:
            for task in self.__tasks:
                archivo.write(f'{task.getName()}|{task.getPriority()}|{task.getState()}')
    
    def openFile(self):
        try:
            with open("tareas.txt","r") as archivo:
                for linea in archivo:
                    name,priority,state = linea.strip().split("|")
                    task = Task(name,priority,state)
                    self.__tasks.append(task)
        except:
            open("tareas.txt","x")
    
   
    
            


