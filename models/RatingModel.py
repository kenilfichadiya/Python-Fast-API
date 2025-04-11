# from pydantic import BaseModel
# from typing import Optional

# class Rating(BaseModel):
#     offerId: str
#     comments: str
#     rating: int

# class RatingOut(Rating):
#     id: str


# from pydantic import BaseModel, Field, validator
# from typing import Optional, Dict, Any
# from bson import ObjectId

# class Rating(BaseModel):
#     comments: str
#     rating: int
#     offer_id: str  # Ensure offer_id is included

# class RatingOut(BaseModel):
#     id: str = Field(alias="_id")
#     comments: str  # Include comments field
#     rating: int
#     offer_id: Optional[str] = None  # Ensure offer_id is optional
#     offer: Optional[Dict[str, Any]] = None  # Ensure offer can be None

#     @validator("id", pre=True, always=True)
#     def convert_objectId(cls, v):
#         if isinstance(v, ObjectId):
#             return str(v)
#         return v   

#     @validator("offer_id", pre=True, always=True)
#     def convert_offer_id(cls, v):
#         if isinstance(v, ObjectId):
#             return str(v)
#         return v

#     @validator("offer", pre=True, always=True)
#     def convert_offer(cls, v):
#         if isinstance(v, dict) and "_id" in v:
#             v["_id"] = str(v["_id"])  # Convert _id inside offer to string
#         return v   


from pydantic import BaseModel, Field, validator
from typing import Optional, Dict, Any
from bson import ObjectId

class Rating(BaseModel):
    comments: str
    rating: int
    offer_id: str  # Ensure offer_id is included

class RatingOut(BaseModel):
    id: str = Field(alias="_id")
    comments: str  # Include comments field
    rating: int
    offer_id: Optional[str] = None  # Ensure offer_id is optional
    offer: Optional[Dict[str, Any]] = None  # Ensure offer can be None

    @validator("id", pre=True, always=True)
    def convert_objectId(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return v   

    @validator("offer_id", pre=True, always=True)
    def convert_offer_id(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return v

    @validator("offer", pre=True, always=True)
    def convert_offer(cls, v):
        if isinstance(v, dict) and "_id" in v:
            v["_id"] = str(v["_id"])  # Convert _id inside offer to string
        return v  