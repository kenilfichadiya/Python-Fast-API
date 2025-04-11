# from fastapi import APIRouter,HTTPException
# from controllers.CityController import deleteCity,addCity#.....
# from models.CityModel import City,CityOut
# from bson import ObjectId

# router = APIRouter()
# @router.post("/city")
# async def post_city(city:City):
#     return await addCity(city)



# @router.get("/city")
# async def get_city():
#     return await getCity()


from fastapi import APIRouter,HTTPException
from controllers.CityController import deleteCity,getCity,addCity
from models.CityModel import City,CityOut
from bson import ObjectId

router = APIRouter()

@router.post("/city/")
async def post_city(city:City):
    return await addCity(city)

@router.get("/city/")
async def get_city():
    return await getCity()

@router.delete("/city/{cityId}")
async def delete_city(cityId:str):
    return await deleteCity(cityId)



