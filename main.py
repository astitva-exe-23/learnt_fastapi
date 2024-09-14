from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List,Optional
from uuid import UUID,uuid4


app = FastAPI()

class Task(BaseModel):
    id: Optional[UUID]=None
    title: str
    description: Optional[str]=None
    completed: bool = False

tasks = []
 
 #POST REQUESTS
@app.post("/tasks/",response_model=Task)
def create_task(task:Task):                #input to the api to create the post request to create the task in questions
    task.id = uuid4()     #each task has an unique identifier
    tasks.append(task)    #append into the empty list called task
    return task   #use the response model to return the task


#GET REQUEST TO EXTRACT TASKS FROM THE TASK LIST
@app.get("/tasks/",response_model=List[Task])
def read_task():
    return tasks


@app.get("/tasls/{task_id}",response_model=Task)
def read_tasks(task_id:UUID):
    for task in tasks:
        if task.id == task_id:
            return task
    
    return HTTPException(status_code=404,detail="Requested Task Was not Found")

#PUT REQUESTS

@app.put("/task/{tasks_id}",response_model=Task)
def update_task(task_id:UUID,task_update:Task):
    for idx,task in enumerate(tasks):
        if task.id == task_id:
            update_task=task.copy(update=task_update.dict(exclude_unset=True))
            tasks[idx] = update_task
            return update_task
        
    raise HTTPException(status_code=404,detail="task not found")


#delete request

@app.delete("/tasks{task_id}/",response_model=Task)
def delete_task(task_id:UUID):
    for idx,task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(idx)
        
    raise HTTPException(status_code=404,detail="task not found")


            

if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)   #0000 IS JUST LOCAL 
