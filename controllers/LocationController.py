# from models.LocationModel import Location, LocationOut
# from bson import ObjectId
# from config.database import location_collection
# from fastapi import HTTPException
# from fastapi.responses import JSONResponse

# async def addLocation(location: Location):
#     savedLocation = await location_collection.insert_one(location.dict(exclude_none=True))
    
#     if not savedLocation.inserted_id:
#         raise HTTPException(status_code=500, detail="Failed to add location")

#     return JSONResponse(content={"message": "Location added successfully"}, status_code=201)

# async def getLocations():
#     Locations = await location_collection.find().to_list(length=100)
    
#     for loc in Locations:
#         loc["id"] = str(loc["_id"])
    
#     return [LocationOut(**loc) for loc in Locations]


# async def deleteLocation(locationId:str):
#     result = await location_collection.delete_one({"_id":ObjectId(locationId)})
#     print("after delete result",result)
#     return {"Message":"Location Deleted Successfully!"}



# from models.LocationModel import Location, LocationOut
# from bson import ObjectId
# from config.database import location_collection
# from fastapi import HTTPException

# async def add_location(location: Location):
#     try:
#         location_dict = location.dict()
#         result = await location_collection.insert_one(location_dict)
#         return {"message": "Location added successfully", "id": str(result.inserted_id)}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error adding location: {str(e)}")

# async def get_locations():
#     try:
#         locations = await location_collection.find().to_list(length=100)
#         for loc in locations:
#             loc["_id"] = str(loc["_id"])  # Convert ObjectId to string
#         return [LocationOut(**loc) for loc in locations]
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error fetching locations: {str(e)}")

# async def delete_location(location_id: str):
#     try:
#         if not ObjectId.is_valid(location_id):
#             raise HTTPException(status_code=400, detail="Invalid location ID")
#         result = await location_collection.delete_one({"_id": ObjectId(location_id)})
#         if result.deleted_count == 0:
#             raise HTTPException(status_code=404, detail="Location not found")
#         return {"message": "Location deleted successfully"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error deleting location: {str(e)}")



from models.LocationModel import Location, LocationOut
from bson import ObjectId
from config.database import location_collection
from fastapi import HTTPException

async def add_location(location: Location):
    try:
        location_dict = location.dict()
        result = await location_collection.insert_one(location_dict)
        return {"message": "Location added successfully", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding location: {str(e)}")

async def get_locations():
    try:
        locations = await location_collection.find().to_list(length=100)
        for loc in locations:
            loc["_id"] = str(loc["_id"])  # Convert ObjectId to string
        return [LocationOut(**loc) for loc in locations]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching locations: {str(e)}")

async def delete_location(location_id: str):
    try:
        if not ObjectId.is_valid(location_id):
            raise HTTPException(status_code=400, detail="Invalid location ID")
        result = await location_collection.delete_one({"_id": ObjectId(location_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Location not found")
        return {"message": "Location deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting location: {str(e)}")