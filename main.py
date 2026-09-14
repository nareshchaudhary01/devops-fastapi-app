from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Success", "message": "DevOps Automated Pipeline Working Properly!"}

@app.get("/health")
def health_check():
    return {"health": "OK", "version": "1.0.0"}