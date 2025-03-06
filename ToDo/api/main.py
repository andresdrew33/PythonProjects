from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Objeto base como modelo de datos
class Task(BaseModel):
    title: str
    description: str
    completed : bool = False

# Diccionario que hace la función de una base de datos
tasks: Dict[int,Task] = {}
task_id_counter=1

# Listar todas las tareas
@app.get("/tasks")
def get_tasks():
    return tasks

# Crear tarea
@app.post("/tasks")
def create_task(task : Task):
    global task_id_counter
    tasks[task_id_counter] = task   
    task_id_counter+=1
    return {'message': "Tarea creada", "task_id": task_id_counter -1}

# Completar tarea
@app.put("/tasks/{task_id}/complete")
def complete_task(task_id : int):
    if task_id not in tasks:
        raise HTTPException(status_code=404,detail="Tarea no encontrada")
    tasks[task_id].completed = True
    return {"message":"Tarea completada"}

# Eliminar tarea
@app.delete("/tasks/{task_id}/delete")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404,detail="Tarea no encontrada")
    del tasks[task_id]
    return {"message":"Tarea eliminada"}
           




