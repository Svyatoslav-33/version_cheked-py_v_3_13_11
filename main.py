from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "FastAPI работает"}

@app.get("hw")
def hello_world():
    return {"massage": "Hello World"}