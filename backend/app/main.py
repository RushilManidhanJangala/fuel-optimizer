from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.fuel_service import calculate_recommendation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/recommendation")
def get_recommendation(start: str, destination: str, mpg: float, gallons: float):
    return calculate_recommendation(mpg, gallons, start, destination)