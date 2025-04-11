from models.AreaModel import Area, AreaOut
from bson import ObjectId
from config.database import area_collection, city_collection, state_collection
from fastapi.responses import JSONResponse
from fastapi import HTTPException, APIRouter

async def deleteArea(areaId:str):
    result = await area_collection.delete_one({"_id":ObjectId(areaId)})
    print("after delete result",result)
    return {"Message":"Area Deleted Successfully!"}
    


async def addArea(area:Area):
    savedArea = await area_collection.insert_one(area.dict())
    return JSONResponse(content={"message:":"Area Added Successfully"},status_code=201)
async def getArea():
    areas = await area_collection.find().to_list(None)


    for area in areas:
        if "city_id" in area and isinstance(area["city_id"], ObjectId):
            area["city_id"] = str(area["city_id"])

        city = await city_collection.find_one({"_id": ObjectId(area["city_id"])}) if area.get("city_id") else None
        
        if city:
            area["_id"] = str(area["_id"])
            city["_id"] = str(city["_id"])
            area["city"] = city  # Attach city details to area

            #  Check if `state_id` exists in the city document before using it
            state_id = city.get("state_id")  # This avoids the NoneType error
            if state_id:
                state = await state_collection.find_one({"_id": ObjectId(state_id)})
                if state:
                    state["_id"] = str(state["_id"])
                    city["state"] = state  # Attach state details to city
                else:
                    city["state"] = None  # Handle missing state case
            else:
                city["state"] = None  # Handle missing state_id case
        else:
            area["city"] = None  # Handle missing city case

    return [AreaOut(**area) for area in areas]





# async def getArea():
#     areas = await area_collection.find().to_list()

#     for area in areas:
#         if "city_id" in area and isinstance(area["city_id"],ObjectId):
#             area["city_id"] = str(area["city_id"])

#         city = await city_collection.find_one({"_id":ObjectId(area["city_id"])})
#         if city:
#             area["_id"] =str(area["_id"])
#             area["city"] = city
        
#         state = await state_collection.find_one({"_id":ObjectId(city["state_id"])})
#         if state:
#             state["_id"] =str(state["_id"])
#             city["state"] = state
#     return [AreaOut(**area) for area in areas]





