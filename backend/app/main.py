from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Fuel Optimizer Backend Running 🚗⛽"}
