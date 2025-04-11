# from pydantic import BaseModel, Field, validator
# from bson import ObjectId
# from typing import Optional

# class Offer(BaseModel):
#     title: str
#     description: str
#     is_active: bool
#     start_date: Optional[str] = None
#     end_date: Optional[str] = None
#     location_id: str  # Foreign key reference

# class OfferOut(Offer):
#     id: str = Field(alias="_id")

#     @validator("id", pre=True, always=True)
#     def convert_object_id(cls, v):
#         if isinstance(v, ObjectId):
#             return str(v)
#         if isinstance(v, str) and ObjectId.is_valid(v):
#             return v
#         raise ValueError("Invalid ObjectId format")



# from pydantic import BaseModel, Field, validator
# from typing import List, Optional, Dict, Any
# from bson import ObjectId

# class Offer(BaseModel):
#     title: str
#     description: str
#     active: bool
#     start_date: Optional[str]
#     end_date: Optional[str]
#     location_id: str
#     food_type: List[str]
#     image_url: Optional[str] = None

# class OfferOut(BaseModel):
#     id: str = Field(alias="_id")
#     title: str
#     description: str
#     active: bool
#     start_date: Optional[str]
#     end_date: Optional[str]
#     location_id: str
#     food_type: List[str]
#     image_url: Optional[str] = None
#     location: Optional[Dict[str, Any]] = None

#     @validator("id", "location_id", pre=True, always=True)
#     def convert_objectid_to_str(cls, v):
#         if isinstance(v, ObjectId):
#             return str(v)
#         return v

#     @validator("location", pre=True, always=True)
#     def convert_nested_objectid(cls, v):
#         if isinstance(v, dict) and "_id" in v:
#             v["_id"] = str(v["_id"])
#         return v



# from pydantic import BaseModel, Field, validator
# from typing import List, Optional, Dict, Any
# from bson import ObjectId
# from datetime import datetime

# class Offer(BaseModel):
#     title: Optional[str]
#     description: Optional[str]
#     discount: Optional[float]
#     start_date: Optional[str]
#     end_date: Optional[str]
#     location_id: str
#     food_type: List[str]
#     image_url: Optional[str] = None

# class OfferOut(BaseModel):
#     id: str = Field(alias="_id")
#     title: Optional[str]
#     description: Optional[str]
#     discount: Optional[float]
#     start_date: Optional[str]
#     end_date: Optional[str]
#     location_id: str
#     food_type: List[str]
#     image_url: Optional[str] = None
#     location: Optional[Dict[str, Any]] = None

#     @validator("id", "location_id", pre=True, always=True)
#     def convert_objectid_to_str(cls, v):
#         if isinstance(v, ObjectId):
#             return str(v)
#         return v

#     @validator("location", pre=True, always=True)
#     def convert_nested_objectid(cls, v):
#         if isinstance(v, dict) and "_id" in v:
#             v["_id"] = str(v["_id"])
#         return v
    
#     @validator("start_date", "end_date", pre=True, always=True)
#     def format_dates(cls, v):
#         if not v:
#             return "Invalid Date"
#         try:
#             return datetime.strptime(v, "%Y-%m-%d").strftime("%d %B %Y")
#         except ValueError:
#             return "Invalid Date"



from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from bson import ObjectId
from datetime import datetime

class Offer(BaseModel):
    title: Optional[str]
    description: Optional[str]
    discount: Optional[float]
    start_date: Optional[str]
    end_date: Optional[str]
    location_id: str
    food_type: List[str] = Field(default_factory=list)  # Ensures default empty list
    image_url: Optional[str] = None

class OfferOut(BaseModel):
    id: str = Field(alias="_id")
    title: Optional[str]
    description: Optional[str]
    discount: Optional[float]
    start_date: Optional[str]
    end_date: Optional[str]
    location_id: str
    food_type: List[str] = Field(default_factory=list)  # Ensures default empty list
    image_url: Optional[str] = None
    location: Optional[Dict[str, Any]] = None

    @validator("id", "location_id", pre=True, always=True)
    def convert_objectid_to_str(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return v

    @validator("location", pre=True, always=True)
    def convert_nested_objectid(cls, v):
        if isinstance(v, dict) and "_id" in v:
            v["_id"] = str(v["_id"])
        return v
    
    @validator("start_date", "end_date", pre=True, always=True)
    def format_dates(cls, v):
        if not v:
            return None
        try:
            return datetime.strptime(v, "%Y-%m-%d").strftime("%d %B %Y")
        except ValueError:
            return None
    
    @validator("food_type", pre=True, always=True)
    def validate_food_type(cls, v):
        if v is None:
            return []  # Converts None to an empty list
        if isinstance(v, str):
            return [v]  # Converts a single string into a list
        if isinstance(v, list):
            return v  # Keeps lists as they are
        raise ValueError("Invalid format for food_type")  # Handles unexpected types
