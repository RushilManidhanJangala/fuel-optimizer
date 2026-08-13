from fastapi import FastAPI
from app.services.fuel_service import calculate_recommendation

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Fuel Optimizer Backend Running 🚗⛽"}


@app.get("/recommendation")
def get_recommendation(
    start: str,
    destination: str,
    mpg: float = 25,
    gallons: float = 10
):
    result = calculate_recommendation(mpg, gallons, start, destination)

    return {
        "route": {
            "start": start,
            "destination": destination
        },
        "inputs": {
            "mpg": mpg,
            "gallons": gallons
        },
        **result
    }
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
