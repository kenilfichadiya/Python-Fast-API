# from config.database import offer_collection
# from bson import ObjectId
# from fastapi import HTTPException
# from fastapi.responses import JSONResponse
# from models.OfferModel import Offer, OfferOut  # Ensure correct import

# async def add_offer(offer: Offer):  # ✅ Function name fixed
#     saved_offer = await offer_collection.insert_one(offer.dict(exclude_none=True))
    
#     if not saved_offer.inserted_id:
#         raise HTTPException(status_code=500, detail="Failed to add offer")

#     return JSONResponse(content={"message": "Offer added successfully"}, status_code=201)

# async def get_offers():  # ✅ Function name fixed
#     offers = await offer_collection.find().to_list(length=100)
    
#     for offer in offers:
#         offer["id"] = str(offer["_id"])
    
#     return [OfferOut(**offer) for offer in offers]

# async def delete_offer(offer_id: str):  # ✅ Function name fixed
#     result = await offer_collection.delete_one({"_id": ObjectId(offer_id)})
    
#     if result.deleted_count == 0:
#         raise HTTPException(status_code=404, detail="Offer not found")

#     return {"message": "Offer deleted successfully!"}


# from models.OfferModel import Offer, OfferOut
# from config.database import offer_collection, location_collection
# from fastapi import HTTPException, UploadFile, File, Form
# from fastapi.responses import JSONResponse
# from bson import ObjectId
# import shutil
# import os
# from utils.CloudinaryUtil import upload_image
# from typing import List

# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# async def create_offer(
#     title: str = Form(...),
#     description: str = Form(...),
#     active: bool = Form(...),
#     start_date: str = Form(...),
#     end_date: str = Form(...),
#     location_id: str = Form(...),
#     food_type: List[str] = Form(...),
#     image: UploadFile = File(...)
# ):
#     try:
#         file_ext = image.filename.split(".")[-1]
#         file_path = os.path.join(UPLOAD_DIR, f"{ObjectId()}.{file_ext}")
#         with open(file_path, "wb") as buffer:
#             shutil.copyfileobj(image.file, buffer)

#         image_url = await upload_image(file_path)
#         offer_data = {
#             "title": title,
#             "description": description,
#             "active": active,
#             "start_date": start_date,
#             "end_date": end_date,
#             "location_id": str(ObjectId(location_id)),
#             "food_type": food_type,
#             "image_url": image_url
#         }
#         await offer_collection.insert_one(offer_data)
#         return JSONResponse(content={"message": "Offer created successfully"}, status_code=201)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# async def get_offers():
#     try:
#         offers = await offer_collection.find().to_list(None)
#         for offer in offers:
#             offer["_id"] = str(offer["_id"])
#             offer["location_id"] = str(offer["location_id"])
#             location = await location_collection.find_one({"_id": ObjectId(offer["location_id"])})
#             if location:
#                 offer["location"] = {"_id": str(location["_id"]), "name": location["name"]}
#         return [OfferOut(**offer) for offer in offers]
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error fetching offers: {str(e)}")




# from models.OfferModel import OfferOut
# from config.database import offer_collection, location_collection
# from fastapi import HTTPException, UploadFile, File, Form
# from fastapi.responses import JSONResponse
# from bson import ObjectId
# import shutil
# import os
# import traceback
# from utils.CloudinaryUtil import upload_image
# from typing import List

# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# async def create_offer(
#     title: str = Form(...),
#     description: str = Form(...),
#     active: bool = Form(...),
#     start_date: str = Form(...),
#     end_date: str = Form(...),
#     location_id: str = Form(...),
#     food_type: List[str] = Form(...),
#     image: UploadFile = File(...)
# ):
#     try:
#         if not ObjectId.is_valid(location_id):
#             raise HTTPException(status_code=400, detail="Invalid location_id format")

#         file_ext = image.filename.split(".")[-1]
#         file_path = os.path.join(UPLOAD_DIR, f"{ObjectId()}.{file_ext}")
#         with open(file_path, "wb") as buffer:
#             shutil.copyfileobj(image.file, buffer)

#         image_url = await upload_image(file_path)

#         offer_data = {
#             "title": title,
#             "description": description,
#             "active": active,
#             "start_date": start_date,
#             "end_date": end_date,
#             "location_id": ObjectId(location_id),
#             "food_type": food_type,
#             "image_url": image_url
#         }

#         result = await offer_collection.insert_one(offer_data)

#         return JSONResponse(content={"message": "Offer created successfully", "offer_id": str(result.inserted_id)}, status_code=201)
#     except Exception as e:
#         print("ERROR in create_offer():", traceback.format_exc())
#         raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


# async def get_offers():
#     try:
#         offers = await offer_collection.find().to_list(None)
#         processed_offers = []

#         for offer in offers:
#             offer["_id"] = str(offer["_id"])
#             offer["location_id"] = str(offer["location_id"]) if "location_id" in offer else None

#             location = None
#             if offer["location_id"] and ObjectId.is_valid(offer["location_id"]):
#                 location = await location_collection.find_one({"_id": ObjectId(offer["location_id"])});

#             offer["location"] = {
#                 "_id": str(location["_id"]) if location else "N/A",
#                 "name": location["name"] if location and "name" in location else "Unknown"
#             }

#             offer.setdefault("active", False)
#             offer.setdefault("food_type", [])
#             offer.setdefault("image_url", None)

#             try:
#                 validated_offer = OfferOut(**offer)
#                 processed_offers.append(validated_offer)
#             except Exception as validation_error:
#                 print("⚠️ Validation Error:", validation_error)
#                 continue

#         return processed_offers

#     except Exception as e:
#         print("ERROR in get_offers():", traceback.format_exc())
#         raise HTTPException(status_code=500, detail=f"Error fetching offers: {str(e)}")




# from models.OfferModel import OfferOut
# from config.database import offer_collection, location_collection
# from fastapi import HTTPException, UploadFile, File, Form
# from fastapi.responses import JSONResponse
# from bson import ObjectId
# import shutil
# import os
# import traceback
# from utils.CloudinaryUtil import upload_image
# from typing import List

# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# async def create_offer(
#     title: str = Form(...),
#     description: str = Form(...),
#     active: bool = Form(...),
#     start_date: str = Form(...),
#     end_date: str = Form(...),
#     location_id: str = Form(...),
#     food_type: List[str] = Form(...),
#     image: UploadFile = File(...)
# ):
#     try:
#         if not ObjectId.is_valid(location_id):
#             raise HTTPException(status_code=400, detail="Invalid location_id format")

#         file_ext = image.filename.split(".")[-1]
#         file_path = os.path.join(UPLOAD_DIR, f"{ObjectId()}.{file_ext}")
#         with open(file_path, "wb") as buffer:
#             shutil.copyfileobj(image.file, buffer)

#         image_url = await upload_image(file_path)

#         offer_data = {
#             "title": title,
#             "description": description,
#             "active": active,
#             "start_date": start_date,
#             "end_date": end_date,
#             "location_id": str(ObjectId(location_id)),
#             "food_type": food_type,
#             "image_url": image_url
#         }

#         result = await offer_collection.insert_one(offer_data)

#         return JSONResponse(content={"message": "Offer created successfully", "offer_id": str(result.inserted_id)}, status_code=201)
#     except Exception as e:
#         print("ERROR in create_offer():", traceback.format_exc())
#         raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


# async def get_offers():
#     try:
#         offers = await offer_collection.find().to_list(None)
#         processed_offers = []

#         for offer in offers:
#             offer["_id"] = str(offer["_id"])
#             offer["location_id"] = str(offer["location_id"]) if "location_id" in offer else None

#             location = None
#             if offer["location_id"] and ObjectId.is_valid(offer["location_id"]):
#                 location = await location_collection.find_one({"_id": ObjectId(offer["location_id"])});

#             offer["location"] = {
#                 "_id": str(location["_id"]) if location else "N/A",
#                 "name": location["name"] if location and "name" in location else "Unknown"
#             }

#             offer.setdefault("active", False)
#             offer.setdefault("food_type", [])
#             offer.setdefault("image_url", None)

#             try:
#                 validated_offer = OfferOut(**offer)
#                 processed_offers.append(validated_offer)
#             except Exception as validation_error:
#                 print("⚠️ Validation Error:", validation_error)
#                 continue

#         return processed_offers

#     except Exception as e:
#         print("ERROR in get_offers():", traceback.format_exc())
#         raise HTTPException(status_code=500, detail=f"Error fetching offers: {str(e)}")




# from models.OfferModel import OfferOut
# from config.database import offer_collection, location_collection
# from fastapi import HTTPException, UploadFile, File, Form
# from fastapi.responses import JSONResponse
# from bson import ObjectId
# import shutil
# import os
# import traceback
# from utils.CloudinaryUtil import upload_image
# from typing import List

# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# async def create_offer(
#     title: str,
#     description: str,
#     discount: float,
#     start_date: str,
#     end_date: str,
#     location_id: str,
#     food_type: List[str],
#     image: UploadFile = None
# ):
#     try:
#         if not ObjectId.is_valid(location_id):
#             raise HTTPException(status_code=400, detail="Invalid location_id format")

#         image_url = "https://example.com/default-image.jpg" # Fallback image

#         if image:
#             file_ext = image.filename.split(".")[-1]
#             file_path = os.path.join(UPLOAD_DIR, f"{ObjectId()}.{file_ext}")
#             with open(file_path, "wb") as buffer:
#                 shutil.copyfileobj(image.file, buffer)
#             image_url = await upload_image(file_path)

#         offer_data = {
#             "title": title,
#             "description": description,
#             "discount": float(discount),
#             "start_date": start_date,
#             "end_date": end_date,
#             "location_id": str(ObjectId(location_id)),
#             "food_type": food_type if food_type else [],
#             "image_url": image_url
#         }

#         result = await offer_collection.insert_one(offer_data)

#         return JSONResponse(content={"message": "Offer created successfully", "offer_id": str(result.inserted_id)}, status_code=201)
#     except Exception as e:
#         print("ERROR in create_offer():", traceback.format_exc())
#         raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# async def get_offers():
#     try:
#         offers = await offer_collection.find().to_list(None)
#         processed_offers = []

#         for offer in offers:
#             offer["_id"] = str(offer["_id"])
#             offer["location_id"] = str(offer["location_id"]) if "location_id" in offer else None

#             location = None
#             if offer["location_id"] and ObjectId.is_valid(offer["location_id"]):
#                 location = await location_collection.find_one({"_id": ObjectId(offer["location_id"])});

#             offer["location"] = location if location else {"_id": "N/A", "name": "Unknown"}

#             offer.setdefault("active", False)
#             offer.setdefault("food_type", [])
#             offer.setdefault("image_url", None)

#             try:
#                 validated_offer = OfferOut(**offer)
#                 processed_offers.append(validated_offer)
#             except Exception as validation_error:
#                 print("⚠️ Validation Error:", validation_error)
#                 continue

#         return processed_offers

#     except Exception as e:
#         print("ERROR in get_offers():", traceback.format_exc())
#         raise HTTPException(status_code=500, detail=f"Error fetching offers: {str(e)}")




# from models.OfferModel import OfferOut
# from config.database import offer_collection, location_collection
# from fastapi import HTTPException, UploadFile, File, Form
# from fastapi.responses import JSONResponse
# from bson import ObjectId
# import shutil
# import os
# import traceback
# from utils.CloudinaryUtil import upload_image
# from typing import List

# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# async def create_offer(
#     title: str,
#     description: str,
#     discount: float,
#     start_date: str,
#     end_date: str,
#     location_id: str,
#     food_type: List[str],
#     image: UploadFile = None
# ):
#     try:
#         if not ObjectId.is_valid(location_id):
#             raise HTTPException(status_code=400, detail="Invalid location_id format")

#         image_url = "https://example.com/default-image.jpg" # Fallback image

#         if image:
#             file_ext = image.filename.split(".")[-1]
#             file_path = os.path.join(UPLOAD_DIR, f"{ObjectId()}.{file_ext}")
#             with open(file_path, "wb") as buffer:
#                 shutil.copyfileobj(image.file, buffer)
#             image_url = await upload_image(file_path)

#         offer_data = {
#             "title": title,
#             "description": description,
#             "discount": float(discount),
#             "start_date": start_date,
#             "end_date": end_date,
#             "location_id": str(ObjectId(location_id)),
#             "food_type": food_type if food_type else [],
#             "image_url": image_url
#         }

#         result = await offer_collection.insert_one(offer_data)

#         return JSONResponse(content={"message": "Offer created successfully", "offer_id": str(result.inserted_id)}, status_code=201)
#     except Exception as e:
#         print("ERROR in create_offer():", traceback.format_exc())
#         raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# async def get_offers():
#     try:
#         offers = await offer_collection.find().to_list(None)
#         processed_offers = []

#         for offer in offers:
#             offer["_id"] = str(offer["_id"])
#             offer["location_id"] = str(offer["location_id"]) if "location_id" in offer else None

#             location = None
#             if offer["location_id"] and ObjectId.is_valid(offer["location_id"]):
#                 location = await location_collection.find_one({"_id": ObjectId(offer["location_id"])})

#             offer["location"] = location if location else {"_id": "N/A", "name": "Unknown"}

#             offer.setdefault("active", False)
#             offer.setdefault("food_type", [])
#             offer.setdefault("image_url", None)

#             try:
#                 validated_offer = OfferOut(**offer)
#                 processed_offers.append(validated_offer)
#             except Exception as validation_error:
#                 print("⚠️ Validation Error:", validation_error)
#                 continue

#         return processed_offers

#     except Exception as e:
#         print("ERROR in get_offers():", traceback.format_exc())
#         raise HTTPException(status_code=500, detail=f"Error fetching offers: {str(e)}")

# # New function to get offer by ID
# async def get_offer_by_id(offer_id: str):
#     try:
#         if not ObjectId.is_valid(offer_id):
#             raise HTTPException(status_code=400, detail="Invalid offer_id format")

#         offer = await offer_collection.find_one({"_id": ObjectId(offer_id)})
#         if not offer:
#             raise HTTPException(status_code=404, detail="Offer not found")

#         offer["_id"] = str(offer["_id"])
#         offer["location_id"] = str(offer["location_id"]) if "location_id" in offer else None

#         # Fetch location details
#         location = None
#         if offer["location_id"] and ObjectId.is_valid(offer["location_id"]):
#             location = await location_collection.find_one({"_id": ObjectId(offer["location_id"])})

#         # offer["location"] = location if location else {"_id": "N/A", "name": "Unknown"}
#         else:
#             offer["location"] = None

#         return OfferOut(**offer)

#     except Exception as e:
#         print("ERROR in get_offer_by_id():", traceback.format_exc())
#         raise HTTPException(status_code=500, detail=f"Error fetching offer details: {str(e)}")





# from models.OfferModel import OfferOut
# from config.database import offer_collection, location_collection
# from fastapi import HTTPException, UploadFile
# from fastapi.responses import JSONResponse
# from bson import ObjectId
# import shutil
# import os
# import traceback
# from utils.CloudinaryUtil import upload_image
# from typing import List

# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# async def create_offer(title: str, description: str, discount: float, start_date: str, end_date: str, location_id: str, food_type: List[str], image: UploadFile = None):
#     try:
#         if not ObjectId.is_valid(location_id):
#             raise HTTPException(status_code=400, detail="Invalid location_id format")

#         image_url = "https://example.com/default-image.jpg"  # Default image

#         if image:
#             file_ext = image.filename.split(".")[-1]
#             file_path = os.path.join(UPLOAD_DIR, f"{ObjectId()}.{file_ext}")
#             with open(file_path, "wb") as buffer:
#                 shutil.copyfileobj(image.file, buffer)
#             image_url = await upload_image(file_path)

#         offer_data = {
#             "title": title,
#             "description": description,
#             "discount": float(discount),
#             "start_date": start_date,
#             "end_date": end_date,
#             "location_id": str(ObjectId(location_id)),
#             "food_type": food_type if food_type else [],
#             "image_url": image_url
#         }

#         result = await offer_collection.insert_one(offer_data)
#         return JSONResponse(content={"message": "Offer created successfully", "offer_id": str(result.inserted_id)}, status_code=201)

#     except Exception as e:
#         print("ERROR in create_offer():", traceback.format_exc())
#         raise HTTPException(status_code=500, detail=str(e))

# # async def get_offers():
# #     try:
# #         offers = await offer_collection.find().to_list(None)
# #         processed_offers = [OfferOut(**{**offer, "_id": str(offer["_id"]), "location_id": str(offer["location_id"])}) for offer in offers]
# #         return processed_offers
# #     except Exception as e:
# #         print("ERROR in get_offers():", traceback.format_exc())
# #         raise HTTPException(status_code=500, detail=str(e))


# async def get_offers():
#     try:
#         offers = await offer_collection.find().to_list(None)
#         processed_offers = []

#         for offer in offers:
#             offer["_id"] = str(offer["_id"])
#             offer["location_id"] = str(offer["location_id"]) if "location_id" in offer else None

#             # Fetch location details correctly
#             location = None
#             if offer["location_id"] and ObjectId.is_valid(offer["location_id"]):
#                 location = await location_collection.find_one({"_id": ObjectId(offer["location_id"])})
                
#                 # Ensure location is not None before assigning
#                 if location:
#                     location["_id"] = str(location["_id"])  # Convert ObjectId to string
#                     offer["location"] = location
#                 else:
#                     offer["location"] = {"_id": "N/A", "name": "Unknown"}

#             offer.setdefault("active", False)
#             offer.setdefault("food_type", [])
#             offer.setdefault("image_url", None)

#             try:
#                 validated_offer = OfferOut(**offer)
#                 processed_offers.append(validated_offer)
#             except Exception as validation_error:
#                 print("⚠️ Validation Error:", validation_error)
#                 continue

#         return processed_offers

#     except Exception as e:
#         print("ERROR in get_offers():", traceback.format_exc())
#         raise HTTPException(status_code=500, detail=f"Error fetching offers: {str(e)}")



# # async def get_offer_by_id(offer_id: str):
# #     try:
# #         if not ObjectId.is_valid(offer_id):
# #             raise HTTPException(status_code=400, detail="Invalid offer_id format")

# #         offer = await offer_collection.find_one({"_id": ObjectId(offer_id)})
# #         if not offer:
# #             raise HTTPException(status_code=404, detail="Offer not found")

# #         return OfferOut(**{**offer, "_id": str(offer["_id"]), "location_id": str(offer["location_id"])})
# #     except Exception as e:
# #         print("ERROR in get_offer_by_id():", traceback.format_exc())
# #         raise HTTPException(status_code=500, detail=str(e))



# async def get_offer_by_id(offer_id):
#     offer = await offer_collection.find_one({"_id": ObjectId(offer_id)})

#     if not offer:
#         return {"error": "Offer not found"}

#     # Fetch location details
#     location = await location_collection.find_one({"_id": ObjectId(offer["location_id"])})

#     if location:
#         offer["location"] = location
#     else:
#         offer["location"] = None

#     # Return formatted offer
#     return OfferOut(**offer)

# async def update_offer(offer_id: str, title: str, description: str, discount: float, start_date: str, end_date: str, food_type: str, image: UploadFile = None):
#     try:
#         if not ObjectId.is_valid(offer_id):
#             raise HTTPException(status_code=400, detail="Invalid offer_id format")

#         update_data = {
#             "title": title,
#             "description": description,
#             "discount": discount,
#             "start_date": start_date,
#             "end_date": end_date,
#             # "location_id": location_id,
#             "food_type": food_type
#         }

#         if image:
#             file_ext = image.filename.split(".")[-1]
#             file_path = os.path.join(UPLOAD_DIR, f"{ObjectId()}.{file_ext}")
#             with open(file_path, "wb") as buffer:
#                 shutil.copyfileobj(image.file, buffer)
#             update_data["image_url"] = await upload_image(file_path)

#         result = await offer_collection.update_one({"_id": ObjectId(offer_id)}, {"$set": update_data})
#         if result.modified_count == 0:
#             raise HTTPException(status_code=404, detail="Offer not found or no change in data")

#         return JSONResponse(content={"message": "Offer updated successfully"}, status_code=200)
#     except Exception as e:
#         print("ERROR in update_offer():", traceback.format_exc())
#         raise HTTPException(status_code=500, detail=str(e))

# async def delete_offer(offer_id: str):
#     try:
#         if not ObjectId.is_valid(offer_id):
#             raise HTTPException(status_code=400, detail="Invalid offer_id format")

#         result = await offer_collection.delete_one({"_id": ObjectId(offer_id)})
#         if result.deleted_count == 0:
#             raise HTTPException(status_code=404, detail="Offer not found")

#         return JSONResponse(content={"message": "Offer deleted successfully"}, status_code=200)
#     except Exception as e:
#         print("ERROR in delete_offer():", traceback.format_exc())
#         raise HTTPException(status_code=500, detail=str(e))

# # New function added here 👇
# async def get_offers_by_food_type(food_type: str):
#     try:
#         # Search for offers that have the specified food_type in their food_type list
#         offers = await offer_collection.find({"food_type": food_type}).to_list(None)
#         processed_offers = []

#         for offer in offers:
#             offer["_id"] = str(offer["_id"])
#             offer["location_id"] = str(offer["location_id"]) if "location_id" in offer else None

#             location = None
#             if offer["location_id"] and ObjectId.is_valid(offer["location_id"]):
#                 location = await location_collection.find_one({"_id": ObjectId(offer["location_id"])})
#                 if location:
#                     location["_id"] = str(location["_id"])
#                     offer["location"] = location
#                 else:
#                     offer["location"] = {"_id": "N/A", "name": "Unknown"}

#             offer.setdefault("active", False)
#             offer.setdefault("food_type", [])
#             offer.setdefault("image_url", None)

#             try:
#                 validated_offer = OfferOut(**offer)
#                 processed_offers.append(validated_offer)
#             except Exception as validation_error:
#                 print("⚠️ Validation Error in get_offers_by_food_type:", validation_error)
#                 continue

#         return processed_offers

#     except Exception as e:
#         print("ERROR in get_offers_by_food_type():", traceback.format_exc())
#         raise HTTPException(status_code=500, detail=str(e))


from models.OfferModel import OfferOut
from config.database import offer_collection, location_collection
from fastapi import HTTPException, UploadFile
from fastapi.responses import JSONResponse
from bson import ObjectId
import shutil
import os
import traceback
from utils.CloudinaryUtil import upload_image
from typing import List

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def create_offer(title: str, description: str, discount: float, start_date: str, end_date: str, location_id: str, food_type: List[str], image: UploadFile = None):
    try:
        if not ObjectId.is_valid(location_id):
            raise HTTPException(status_code=400, detail="Invalid location_id format")

        image_url = "https://example.com/default-image.jpg"

        if image:
            file_ext = image.filename.split(".")[-1]
            file_path = os.path.join(UPLOAD_DIR, f"{ObjectId()}.{file_ext}")
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(image.file, buffer)
            image_url = await upload_image(file_path)

        offer_data = {
            "title": title,
            "description": description,
            "discount": float(discount),
            "start_date": start_date,
            "end_date": end_date,
            "location_id": str(ObjectId(location_id)),
            "food_type": food_type if food_type else [],
            "image_url": image_url
        }

        result = await offer_collection.insert_one(offer_data)
        return JSONResponse(content={"message": "Offer created successfully", "offer_id": str(result.inserted_id)}, status_code=201)

    except Exception as e:
        print("ERROR in create_offer():", traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))


async def get_offers():
    try:
        offers = await offer_collection.find().to_list(None)
        processed_offers = []

        for offer in offers:
            offer["_id"] = str(offer["_id"])
            offer["location_id"] = str(offer["location_id"]) if "location_id" in offer else None

            location = None
            if offer["location_id"] and ObjectId.is_valid(offer["location_id"]):
                location = await location_collection.find_one({"_id": ObjectId(offer["location_id"])})
                offer["location"] = location if location else {"_id": "N/A", "name": "Unknown"}

            offer.setdefault("active", False)
            offer.setdefault("food_type", [])
            offer.setdefault("image_url", None)

            try:
                validated_offer = OfferOut(**offer)
                processed_offers.append(validated_offer)
            except Exception as validation_error:
                print("⚠️ Validation Error:", validation_error)
                continue

        return processed_offers

    except Exception as e:
        print("ERROR in get_offers():", traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Error fetching offers: {str(e)}")


async def get_offer_by_id(offer_id):
    offer = await offer_collection.find_one({"_id": ObjectId(offer_id)})

    if not offer:
        return {"error": "Offer not found"}

    location = await location_collection.find_one({"_id": ObjectId(offer["location_id"])})
    offer["location"] = location if location else None

    return OfferOut(**offer)


async def update_offer(offer_id: str, title: str, description: str, discount: float, start_date: str, end_date: str, food_type: str, image: UploadFile = None):
    try:
        if not ObjectId.is_valid(offer_id):
            raise HTTPException(status_code=400, detail="Invalid offer_id format")

        update_data = {
            "title": title,
            "description": description,
            "discount": discount,
            "start_date": start_date,
            "end_date": end_date,
            "food_type": food_type
        }

        if image:
            file_ext = image.filename.split(".")[-1]
            file_path = os.path.join(UPLOAD_DIR, f"{ObjectId()}.{file_ext}")
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(image.file, buffer)
            update_data["image_url"] = await upload_image(file_path)

        result = await offer_collection.update_one({"_id": ObjectId(offer_id)}, {"$set": update_data})
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Offer not found or no change in data")

        return JSONResponse(content={"message": "Offer updated successfully"}, status_code=200)
    except Exception as e:
        print("ERROR in update_offer():", traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))


async def delete_offer(offer_id: str):
    try:
        if not ObjectId.is_valid(offer_id):
            raise HTTPException(status_code=400, detail="Invalid offer_id format")

        result = await offer_collection.delete_one({"_id": ObjectId(offer_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Offer not found")

        return JSONResponse(content={"message": "Offer deleted successfully"}, status_code=200)
    except Exception as e:
        print("ERROR in delete_offer():", traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))


async def get_offers_by_food_type(food_type: str):
    try:
        offers = await offer_collection.find({"food_type": food_type}).to_list(None)
        processed_offers = []

        for offer in offers:
            offer["_id"] = str(offer["_id"])
            offer["location_id"] = str(offer["location_id"]) if "location_id" in offer else None

            location = None
            if offer["location_id"] and ObjectId.is_valid(offer["location_id"]):
                location = await location_collection.find_one({"_id": ObjectId(offer["location_id"])})
                offer["location"] = location if location else {"_id": "N/A", "name": "Unknown"}

            offer.setdefault("active", False)
            offer.setdefault("food_type", [])
            offer.setdefault("image_url", None)

            try:
                validated_offer = OfferOut(**offer)
                processed_offers.append(validated_offer)
            except Exception as validation_error:
                print("⚠️ Validation Error in get_offers_by_food_type:", validation_error)
                continue

        return processed_offers

    except Exception as e:
        print("ERROR in get_offers_by_food_type():", traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))


# ⭐ NEW FUNCTION: Get best deals (discount >= 30%)
async def get_best_deals():
    try:
        offers = await offer_collection.find({"discount": {"$gte": 40}}).to_list(None)
        processed_offers = []

        for offer in offers:
            offer["_id"] = str(offer["_id"])
            offer["location_id"] = str(offer["location_id"]) if "location_id" in offer else None

            location = None
            if offer["location_id"] and ObjectId.is_valid(offer["location_id"]):
                location = await location_collection.find_one({"_id": ObjectId(offer["location_id"])})
                offer["location"] = location if location else {"_id": "N/A", "name": "Unknown"}

            offer.setdefault("active", False)
            offer.setdefault("food_type", [])
            offer.setdefault("image_url", None)

            try:
                validated_offer = OfferOut(**offer)
                processed_offers.append(validated_offer)
            except Exception as validation_error:
                print("⚠️ Validation Error in get_best_deals:", validation_error)
                continue

        return processed_offers
    except Exception as e:
        print("ERROR in get_best_deals():", traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
