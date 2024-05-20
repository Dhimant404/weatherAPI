from typing import List
from bson import ObjectId
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGODB_URL
from app.utils.caching import deleteCache


class Location(BaseModel):
    name: str
    latitude: float
    longitude: float


router = APIRouter()

client = AsyncIOMotorClient(MONGODB_URL)
db = client.weather


@router.post("/", response_model=Location)
async def createLocation(location: Location):
    """
    Create a new location.
    """
    newLocation = await db.locations.insert_one(location.dict())
    createdLocation = await db.locations.find_one({"_id": newLocation.inserted_id})
    return createdLocation


@router.get("/", response_model=List[Location])
async def getLocations():
    """
    Retrieve all locations.
    """
    locations = await db.locations.find().to_list(1000)
    return locations


@router.get("/{locationId}", response_model=Location)
async def getLocation(locationId: str):
    """
    Retrieve a location by ID.
    """
    location = await db.locations.find_one({"_id": ObjectId(locationId)})
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location


@router.put("/{locationId}", response_model=Location)
async def updateLocation(locationId: str, location: Location):
    """
    Update a location by ID.
    """
    await db.locations.update_one(
        {"_id": ObjectId(locationId)}, {"$set": location.dict()}
    )
    updatedLocation = await db.locations.find_one({"_id": ObjectId(locationId)})
    if not updatedLocation:
        raise HTTPException(status_code=404, detail="Location not found")

    # Invalidate cache
    await deleteCache(f"weather:{locationId}")

    return updatedLocation


@router.delete("/{locationId}", response_model=dict)
async def deleteLocation(locationId: str):
    """
    Delete a location by ID.
    """
    if not ObjectId.is_valid(locationId):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    result = await db.locations.delete_one({"_id": ObjectId(locationId)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Location not found")

    # Invalidate cache
    await deleteCache(f"weather:{locationId}")

    return {"message": "Location deleted successfully"}
