#FastAPI - example 


from fastapi import FastAPI 

app=FastAPI()

@app.get("/msg")
def hello():
    return {"message":"Welcome to FastAPI"}

@app.get("/add")
def hi(a:int, b:int):
    return {"result":a+b}

#http://127.0.0.1:8000/msg
#http://127.0.0.1:8000/add?a=5&b=10
