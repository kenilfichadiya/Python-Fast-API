# from pydantic import BaseModel, Field, validator
# from bson import ObjectId

# class Location(BaseModel):
#     location: str = Field(default="Unknown Location")  # Default value
#     title: str = Field(default="")
#     category: str = Field(default="")
#     description: str = Field(default="")
#     timing: str = Field(default="")
#     is_active: bool = Field(default=True)  # Default boolean

#     @validator("location", pre=True, always=True)
#     def ensure_location_is_string(cls, v):
#         if isinstance(v, bool):  # Convert boolean to string
#             return "Unknown Location"
#         return str(v)  # Ensure it's always a string

# class LocationOut(Location):
#     id: str = Field(..., alias="_id")

#     @validator("id", pre=True, always=True)
#     def convert_object_id(cls, v):
#         if isinstance(v, ObjectId):
#             return str(v)
#         if isinstance(v, str) and ObjectId.is_valid(v):
#             return v
#         raise ValueError("Invalid ObjectId format")




from pydantic import BaseModel, Field, validator
from bson import ObjectId

class Location(BaseModel):
    restaurant: str =Field(default="")
    location: str = Field(default="Unknown Location")
    city: str = Field (default="")
    state: str= Field(default="")
    category: str = Field(default="")
    description: str = Field(default="")
    timing: str = Field(default="")
    

    @validator("location", pre=True, always=True)
    def ensure_location_is_string(cls, v):
        if isinstance(v, bool):
            return "Unknown Location"
        return str(v)

class LocationOut(Location):
    id: str = Field(..., alias="_id")

    @validator("id", pre=True, always=True)
    def convert_object_id(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        if isinstance(v, str) and ObjectId.is_valid(v):
            return v
        raise ValueError("Invalid ObjectId format")
