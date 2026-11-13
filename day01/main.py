from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    name: str
    age:int 
    skills: list


store= {}
next_id=1

@app.get("/health")
def health_check():
    return {"message":"health check"}

@app.get("/about/{user_name}")
def what_about(user_name: str):
    return {"message":f"hi , how are you {user_name}"}

@app.post("/postdata")
def postdata(data: User):
    global next_id
    store[next_id]= data
    new_id=next_id
    next_id+=1
    return {"message":"success","id":new_id,
        "data": store}

@app.put("/updatedata/{user_id}")
def update_data(user_id: int, data:User):
    if user_id not in store:
        return {"message":"user not found"}
    else:
        store[user_id]=data
        return {"message":"data updated",
        "data": store}

@app.delete("/deletdata/{user_id}")
def delete_data(user_id: int):
    if user_id not in store:
        return {"message":"user not found"}
    else:
        removed=store.pop(user_id)
        return {"message":"data deleted",
        "data": removed,
        "store": store}