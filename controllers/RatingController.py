# from config.database import rating_collection
# from models.RatingModel import Rating, RatingOut
# from bson import ObjectId
# from fastapi import HTTPException
# from fastapi.responses import JSONResponse


# async def add_rating(rating: Rating):
#     new_rating = await rating_collection.insert_one(rating.dict())
#     if not new_rating.inserted_id:
#         raise HTTPException(status_code=500, detail="Failed to add rating")
    
#     return JSONResponse(content={"message": "Rating added successfully"}, status_code=201)

# async def get_ratings():
#     ratings = await rating_collection.find().to_list(100)
#     return [{"id": str(r["_id"]), **r} for r in ratings]

# async def delete_rating(rating_id: str):
#     result = await rating_collection.delete_one({"_id": ObjectId(rating_id)})
#     if result.deleted_count == 0:
#         raise HTTPException(status_code=404, detail="Rating not found")
    
#     return {"message": "Rating deleted successfully"}


# from models.RatingModel import Rating,RatingOut
# from bson import ObjectId
# from fastapi.responses import JSONResponse
# from fastapi import HTTPException
# from config.database import rating_collection,offer_collection

# async def add_rating(rating:Rating):
#     savedRating = await rating_collection.insert_one(rating.dict())
#     if savedRating:
#         return JSONResponse(status_code=201,content={"message:":"Rating Added Successfully"})
#     raise HTTPException(status_code=500,detail="Internal Server Error")

# async def get_ratings():
#     ratings = await rating_collection.find().to_list()
#     #check lennght of states
#     for rating in ratings:
#         if "offer_id" in rating and isinstance(rating["offer_if"], ObjectId):
#             rating["offer_id"] =str(rating["offer_id"])
#         offer =await offer_collection.find_one({"-id":ObjectId(rating["offer_id"])})    
#         if offer:
#             offer["_id"] =str(offer["_id"])
#             rating["offer"]=offer
    
#     return [RatingOut(**rating) for rating in ratings]

    

# async def delete_rating(ratingId:str):
#     result = await rating_collection.delete_one({"_id":ObjectId(ratingId)})
#     print("after delete result",result)
#     return {"Message":"rating Deleted Successfully!"}



# from models.RatingModel import Rating, RatingOut
# from bson import ObjectId
# from fastapi.responses import JSONResponse
# from fastapi import HTTPException
# from config.database import rating_collection, offer_collection

# async def add_rating(rating: Rating):
#     try:
#         saved_rating = await rating_collection.insert_one(rating.dict())
#         if saved_rating:
#             return JSONResponse(status_code=201, content={"message": "Rating Added Successfully"})
#         raise HTTPException(status_code=500, detail="Internal Server Error")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# async def get_ratings():
#     try:
#         ratings = await rating_collection.find().to_list(None)  # Fixed syntax

#         for rating in ratings:
#             rating["_id"] = str(rating["_id"])  # Convert ObjectId to string

#             # Ensure 'offer_id' exists before processing
#             if "offer_id" in rating and isinstance(rating["offer_id"], (str, ObjectId)):
#                 if isinstance(rating["offer_id"], ObjectId):
#                     rating["offer_id"] = str(rating["offer_id"])  # Convert to string

#                 # Validate and fetch the offer details
#                 if ObjectId.is_valid(rating["offer_id"]):
#                     offer = await offer_collection.find_one({"_id": ObjectId(rating["offer_id"])})
#                     if offer:
#                         offer["_id"] = str(offer["_id"])  # Convert ObjectId to string
#                         rating["offer"] = offer
#                     else:
#                         rating["offer"] = None  # If offer not found
#                 else:
#                     rating["offer"] = None  # If invalid ObjectId
#             else:
#                 rating["offer_id"] = None  # Handle missing offer_id

#         return [RatingOut(**rating) for rating in ratings]

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# async def delete_rating(rating_id: str):
#     try:
#         result = await rating_collection.delete_one({"_id": ObjectId(rating_id)})
#         if result.deleted_count == 1:
#             return {"message": "Rating Deleted Successfully!"}
#         raise HTTPException(status_code=404, detail="Rating not found")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))



# from models.RatingModel import Rating, RatingOut
# from bson import ObjectId
# from fastapi.responses import JSONResponse
# from fastapi import HTTPException
# from config.database import rating_collection, offer_collection

# async def add_rating(rating: Rating):
#     savedRating = await rating_collection.insert_one(rating.dict())
#     if savedRating:
#         return JSONResponse(status_code=201, content={"message": "Rating Added Successfully"})
#     raise HTTPException(status_code=500, detail="Internal Server Error")

# async def get_ratings():
#     ratings = await rating_collection.find().to_list(None)

#     for rating in ratings:
#         # Convert _id to string
#         rating["_id"] = str(rating["_id"])

#         # Ensure offer_id is a valid ObjectId
#         if "offer_id" in rating and rating["offer_id"]:
#             try:
#                 offer_id = ObjectId(rating["offer_id"])  # Convert to ObjectId
#                 offer = await offer_collection.find_one({"_id": offer_id}, {"_id": 1, "offer_name": 1})  # Fetch only necessary fields

#                 if offer:
#                     offer["_id"] = str(offer["_id"])  # Convert offer _id to string
#                     rating["offer"] = {"id": offer["_id"], "name": offer.get("offer_name", "Unknown")}
#                 else:
#                     rating["offer"] = {"id": rating["offer_id"], "name": "Not Found"}
#             except Exception as e:
#                 rating["offer"] = {"id": rating["offer_id"], "name": "Invalid Offer ID"}

#     return [RatingOut(**rating) for rating in ratings]

# async def delete_rating(ratingId: str):
#     try:
#         object_id = ObjectId(ratingId)  # Ensure valid ObjectId
#     except:
#         raise HTTPException(status_code=400, detail="Invalid Rating ID")

#     result = await rating_collection.delete_one({"_id": object_id})
#     if result.deleted_count == 1:
#         return {"message": "Rating Deleted Successfully"}
#     raise HTTPException(status_code=404, detail="Rating not found")


# from models.RatingModel import Rating, RatingOut
# from bson import ObjectId
# from config.database import rating_collection
# from fastapi import HTTPException
# from fastapi.responses import JSONResponse

# async def add_rating(rating: Rating):
#     saved_rating = await rating_collection.insert_one(rating.dict(exclude_none=True))
    
#     if not saved_rating.inserted_id:
#         raise HTTPException(status_code=500, detail="Failed to add rating")

#     return JSONResponse(content={"message": "Rating added successfully"}, status_code=201)

# async def get_ratings():
#     ratings = await rating_collection.find().to_list(length=100)
    
#     for rate in ratings:
#         rate["id"] = str(rate["_id"])
    
#     return [RatingOut(**rate) for rate in ratings]

# async def delete_rating(rating_id: str):
#     if not ObjectId.is_valid(rating_id):
#         raise HTTPException(status_code=400, detail="Invalid rating ID")
    
#     result = await rating_collection.delete_one({"_id": ObjectId(rating_id)})
    
#     if result.deleted_count == 0:
#         raise HTTPException(status_code=404, detail="Rating not found")
    
#     return {"message": "Rating deleted successfully"}




from models.RatingModel import Rating, RatingOut
from bson import ObjectId
from config.database import rating_collection, offer_collection  # Make sure offer_collection is imported
from fastapi import HTTPException
from fastapi.responses import JSONResponse

async def add_rating(rating: Rating):
    saved_rating = await rating_collection.insert_one(rating.dict(exclude_none=True))
    
    if not saved_rating.inserted_id:
        raise HTTPException(status_code=500, detail="Failed to add rating")

    return JSONResponse(content={"message": "Rating added successfully"}, status_code=201)

async def get_ratings():
    ratings = await rating_collection.find().to_list(length=100)
    
    for rate in ratings:
        rate["id"] = str(rate["_id"])

        # Fetch the offer details based on offer_id
        if "offer_id" in rate and rate["offer_id"]:
            offer = await offer_collection.find_one({"_id": ObjectId(rate["offer_id"])})
            if offer:
                offer["_id"] = str(offer["_id"])  # Convert ObjectId to string
                rate["offer"] = offer
            else:
                rate["offer"] = None
        else:
            rate["offer"] = None

    return [RatingOut(**rate) for rate in ratings]

async def delete_rating(rating_id: str):
    if not ObjectId.is_valid(rating_id):
        raise HTTPException(status_code=400, detail="Invalid rating ID")
    
    result = await rating_collection.delete_one({"_id": ObjectId(rating_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Rating not found")
    
    return {"message": "Rating deleted successfully"}
