import httpx
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGODB_URL, WEATHER_API_URL, WEATHER_API_KEY
from bson import ObjectId

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGODB_URL)
db = client.weather


async def fetchWeather(locationId: str):
    """
    Get weather data from external API (Open weather map API).
    """
    location = await db.locations.find_one({"_id": ObjectId(locationId)})
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    params = {
        "lat": location["latitude"],
        "lon": location["longitude"],
        "appid": WEATHER_API_KEY,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(WEATHER_API_URL, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()
