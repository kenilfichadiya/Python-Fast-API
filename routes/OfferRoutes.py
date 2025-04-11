# from fastapi import APIRouter
# from controllers.OfferController import add_offer, get_offers, delete_offer  # ✅ Fixed imports
# from models.OfferModel import Offer, OfferOut
# from typing import List

# router = APIRouter(prefix="/offers", tags=["Offers"])

# @router.post("/", response_model=dict)
# async def create_offer(offer: Offer):
#     return await add_offer(offer)  # ✅ Function name fixed

# @router.get("/", response_model=List[OfferOut])
# async def fetch_offers():
#     return await get_offers()  # ✅ Function name fixed

# @router.delete("/{offer_id}")
# async def remove_offer(offer_id: str):
#     return await delete_offer(offer_id)  # ✅ Function name fixed



# from fastapi import APIRouter, Form, UploadFile, File
# from controllers.OfferController import create_offer, get_offers

# router = APIRouter()

# @router.post("/create_offer")
# async def create_offer_route(
#     title: str = Form(...),
#     description: str = Form(...),
#     active: bool = Form(...),
#     start_date: str = Form(...),
#     end_date: str = Form(...),
#     location_id: str = Form(...),
#     food_type: list = Form(...),
#     image: UploadFile = File(...)
# ):
#     return await create_offer(title, description, active, start_date, end_date, location_id, food_type, image)

# @router.get("/get_offers")
# async def get_offers_route():
#     return await get_offers()



# from fastapi import APIRouter, Form, UploadFile, File
# from controllers.OfferController import create_offer, get_offers

# router = APIRouter()

# @router.post("/create_offer")
# async def create_offer_route(
#     title: str = Form(...),
#     description: str = Form(...),
#     discount: float = Form(...),
#     start_date: str = Form(...),
#     end_date: str = Form(...),
#     location_id: str = Form(...),
#     food_type: list = Form(...),
#     image: UploadFile = File(None)
# ):
#     return await create_offer(title, description, discount, start_date, end_date, location_id, food_type, image)

# @router.get("/get_offers")
# async def get_offers_route():
#     return await get_offers()




# from fastapi import APIRouter, Form, UploadFile, File
# from controllers.OfferController import create_offer, get_offers, get_offer_by_id

# router = APIRouter()

# @router.post("/create_offer")
# async def create_offer_route(
#     title: str = Form(...),
#     description: str = Form(...),
#     discount: float = Form(...),
#     start_date: str = Form(...),
#     end_date: str = Form(...),
#     location_id: str = Form(...),
#     food_type: list = Form(...),
#     image: UploadFile = File(None)
# ):
#     return await create_offer(title, description, discount, start_date, end_date, location_id, food_type, image)

# @router.get("/get_offers")
# async def get_offers_route():
#     return await get_offers()

# # New Route for fetching offer by ID
# @router.get("/offers/{offer_id}")
# async def get_offer_by_id_route(offer_id: str):
#     return await get_offer_by_id(offer_id)




# from fastapi import APIRouter, Form, UploadFile, File
# from controllers.OfferController import (
#     create_offer,
#     get_offers,
#     get_offer_by_id,
#     update_offer,
#     delete_offer,
#     get_offers_by_food_type
# )

# router = APIRouter()

# @router.post("/create_offer")
# async def create_offer_route(
#     title: str = Form(...),
#     description: str = Form(...),
#     discount: float = Form(...),
#     start_date: str = Form(...),
#     end_date: str = Form(...),
#     location_id: str = Form(...),
#     food_type: list = Form(...),
#     image: UploadFile = File(None)
# ):
#     return await create_offer(
#         title, description, discount, start_date, end_date, location_id, food_type, image
#     )

# @router.get("/get_offers")
# async def get_offers_route():
#     return await get_offers()

# @router.get("/offers/{offer_id}")
# async def get_offer_by_id_route(
#     offer_id: str
# ):
#     return await get_offer_by_id(offer_id)

# @router.put("/update_offer/{offer_id}")
# async def update_offer_route(
#     offer_id: str,
#     title: str = Form(...),
#     description: str = Form(...),
#     discount: float = Form(...),
#     start_date: str = Form(...),
#     end_date: str = Form(...),
#     food_type: str = Form(...),
#     image: UploadFile = File(None)
# ):
#     return await update_offer(
#         offer_id, title, description, discount, start_date, end_date,  food_type, image
#     )

# @router.delete("/delete_offer/{offer_id}")
# async def delete_offer_route(
#     offer_id: str
# ):
#     return await delete_offer(offer_id)


# @router.get("/offers/food_type/{food_type}")
# async def get_offers_by_food_type_route(food_type: str):
#     return await get_offers_by_food_type(food_type)


from fastapi import APIRouter, Form, UploadFile, File
from controllers.OfferController import (
    create_offer,
    get_offers,
    get_offer_by_id,
    update_offer,
    delete_offer,
    get_offers_by_food_type,
    get_best_deals  # ✅ Include the new controller function
)

router = APIRouter()

@router.post("/create_offer")
async def create_offer_route(
    title: str = Form(...),
    description: str = Form(...),
    discount: float = Form(...),
    start_date: str = Form(...),
    end_date: str = Form(...),
    location_id: str = Form(...),
    food_type: list = Form(...),
    image: UploadFile = File(None)
):
    return await create_offer(
        title, description, discount, start_date, end_date, location_id, food_type, image
    )

@router.get("/get_offers")
async def get_offers_route():
    return await get_offers()

# ✅ Place fixed/static routes BEFORE dynamic ones

@router.get("/offers/best_deals")
async def get_best_deals_route():
    return await get_best_deals()

@router.get("/offers/food_type/{food_type}")
async def get_offers_by_food_type_route(food_type: str):
    return await get_offers_by_food_type(food_type)

# 🛑 Keep this last to avoid conflict with 'best_deals' or 'food_type/...'
@router.get("/offers/{offer_id}")
async def get_offer_by_id_route(offer_id: str):
    return await get_offer_by_id(offer_id)

@router.put("/update_offer/{offer_id}")
async def update_offer_route(
    offer_id: str,
    title: str = Form(...),
    description: str = Form(...),
    discount: float = Form(...),
    start_date: str = Form(...),
    end_date: str = Form(...),
    food_type: str = Form(...),
    image: UploadFile = File(None)
):
    return await update_offer(
        offer_id, title, description, discount, start_date, end_date, food_type, image
    )

@router.delete("/delete_offer/{offer_id}")
async def delete_offer_route(offer_id: str):
    return await delete_offer(offer_id)
