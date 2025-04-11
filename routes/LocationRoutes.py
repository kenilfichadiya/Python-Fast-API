from fastapi import APIRouter, HTTPException
from controllers.LocationController import add_location, get_locations, delete_location
from models.LocationModel import Location, LocationOut
from typing import List

router = APIRouter(prefix="/locations")

@router.post("/", response_model=dict)
async def add_location_route(location: Location):
    try:
        return await add_location(location)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[LocationOut])
async def get_locations_route():
    try:
        return await get_locations()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{location_id}")
async def delete_location_route(location_id: str):
    try:
        return await delete_location(location_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
