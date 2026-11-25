#FastAPI - example (GET, POST, PUT, PATCH)


from fastapi import FastAPI 

app=FastAPI()
values={"a":10,"b":5}

#GET...
@app.get("/msg")
def hello():
    return {"message":"Welcome to FastAPI"}
@app.get("/add")
def Add(a:int, b:int):
    return {"result":a+b}

#POST...CREATE NEW VALUES
@app.post("/values")
def Create(a:int, b:int):
    values["a"]=a 
    values["b"]=b
    return {"result":values}
    
#PUT...REPLACE ALL - OLD DELETED COMPLETELY
@app.put("/values")
def Replace(a:int, b:int):
    values["a"]=a 
    values["b"]=b
    return {"result":values}
    
#PATCH...UPDATE ONLY ONE
@app.patch("/values")
def Update(a:int | None=None, b:int|None=None):
    if a is not None:
        values["a"]=a 
    if b is not None: 
        values["b"]=b
    return {"result":values}


#http://127.0.0.1:8000/msg
#http://127.0.0.1:8000/add?a=5&b=10
#http://127.0.0.1:8000/docs


#pip install "fastapi[standard]"
#uv run fastapi dev fast_api.py
#uv run uvicorn fastapi_methods:app --reload
