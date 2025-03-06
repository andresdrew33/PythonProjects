from gestor import Gestor

gestor = Gestor()

gestor.openFile()

gestor.addTask("Tarea 1",4)
gestor.addTask("Tarea 2",5)
gestor.addTask("Tarea 3",6)
gestor.addTask("Tarea 4",10)

gestor.showTasks()

gestor.completeTask("Tarea 1")
gestor.completeTask("Tarea 2")

gestor.showTasks()

gestor.saveInFile()
