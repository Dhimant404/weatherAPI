from fastapi import APIRouter, HTTPException
from app.services.weatherService import fetchWeather
from app.utils.caching import getCache, setCache
from app.config import WEATHER_API_URL, WEATHER_API_KEY, MONGODB_URL

router = APIRouter()


@router.get("/{locationId}")
async def getWeather(locationId: str):
    """
    Get weather data from eithe cache or external API.
    """
    # Check cache
    cachedWeather = await getCache(f"weather:{locationId}")
    if cachedWeather:
        return cachedWeather
    # Fetch weather from external API
    weatherData = await fetchWeather(locationId)
    if not weatherData:
        raise HTTPException(status_code=500, detail="Weather service unavailable")
    # Set cache
    await setCache(f"weather:{locationId}", weatherData, ttl=60)  # Cache for 1 minutes
    return weatherData
