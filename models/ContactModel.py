from pydantic import BaseModel, Field, validator
from typing import Optional, Dict, Any
from bson import ObjectId

class Contact(BaseModel):
    address: str
    city_id: str
    area_id: str
    food_type: str
    latitude: float
    longitude: float

class ContactOut(Contact):
    id: str = Field(alias="_id")
    city: Optional[Dict[str, Any]] = None
    area: Optional[Dict[str, Any]] = None

    @validator("id", pre=True, always=True)
    def convert_objectId(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return v

    @validator("city", "area", pre=True, always=True)
    def convert_objectId_in_nested(cls, v):
        if isinstance(v, dict) and "_id" in v:
            v["_id"] = str(v["_id"])
        return v
