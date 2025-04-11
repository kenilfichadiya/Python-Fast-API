# from fastapi import APIRouter
# from controllers.RatingController import add_rating, get_ratings, delete_rating
# from models.RatingModel import Rating, RatingOut
# from typing import List

# router = APIRouter(prefix="/ratings", tags=["Ratings"])

# @router.post("/", response_model=dict)
# async def create_rating(rating: Rating):
#     return await add_rating(rating)

# @router.get("/", response_model=List[RatingOut])
# async def fetch_ratings():
#     return await get_ratings()

# @router.delete("/{rating_id}")
# async def remove_rating(rating_id: str):
#     return await delete_rating(rating_id)


# from fastapi import APIRouter
# from controllers.RatingController import add_rating, get_ratings, delete_rating
# from models.RatingModel import Rating, RatingOut
# from typing import List

# router = APIRouter(prefix="/ratings", tags=["Ratings"])



# @router.post("/", response_model=dict)
# async def create_rating(rating: Rating):
#     return await add_rating(rating)

# @router.get("/", response_model=List[RatingOut])
# async def fetch_ratings():
#     return await get_ratings()

# @router.delete("/{rating_id}")
# async def remove_rating(rating_id: str):
#     return await delete_rating(rating_id)



# from fastapi import APIRouter
# from controllers.RatingController import add_rating, get_ratings, delete_rating
# from models.RatingModel import Rating, RatingOut

# router = APIRouter()

# @router.post("/addrating/")
# async def create_rating(rating: Rating):
#     return await add_rating(rating)  # ✅ Call the correct function

# @router.get("/getrating/")
# async def fetch_ratings():
#     return await get_ratings()  # ✅ Call the controller function

# @router.delete("/rating/{ratingId}")
# async def delete_rating(ratingId: str):
#     return await delete_rating(ratingId)  # ✅ Call the controller function





from fastapi import APIRouter
from controllers.RatingController import add_rating, get_ratings, delete_rating
from models.RatingModel import Rating, RatingOut

router = APIRouter()

@router.post("/addrating/")
async def create_rating(rating: Rating):
    return await add_rating(rating)

@router.get("/getrating/")
async def fetch_ratings():
    return await get_ratings()

@router.delete("/rating/{ratingId}")
async def delete_rating_route(ratingId: str):
    return await delete_rating(ratingId)




