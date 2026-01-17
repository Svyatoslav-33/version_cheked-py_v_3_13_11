from fastapi import FastAPI 

app = FastAPI()

@app.get("/")  
async def root():  
    return {"message": "API работает!"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}