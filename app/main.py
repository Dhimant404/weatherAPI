from fastapi import FastAPI
from app.routes import location, weather

app = FastAPI()

app.include_router(location.router, prefix="/locations", tags=["locations"])
app.include_router(weather.router, prefix="/weather", tags=["weather"])


@app.get("/")
async def root():
    return {"message": "Welcome to the Weather Forecast API!"}
