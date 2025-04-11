from models.ContactModel import Contact, ContactOut
from bson import ObjectId
from config.database import contact_collection, city_collection, area_collection
from fastapi import HTTPException
from fastapi.responses import JSONResponse

async def addContact(contact: Contact):
    savedContact = await contact_collection.insert_one(contact.dict())
    return JSONResponse(content={"message": "Contact Added Successfully"}, status_code=201)

async def getContacts():
    contacts = await contact_collection.find().to_list(None)

    for contact in contacts:
        if "city_id" in contact and isinstance(contact["city_id"], ObjectId):
            contact["city_id"] = str(contact["city_id"])
        if "area_id" in contact and isinstance(contact["area_id"], ObjectId):
            contact["area_id"] = str(contact["area_id"])

        city = await city_collection.find_one({"_id": ObjectId(contact["city_id"])}) if contact.get("city_id") else None
        area = await area_collection.find_one({"_id": ObjectId(contact["area_id"])}) if contact.get("area_id") else None
        
        if city:
            city["_id"] = str(city["_id"])
            contact["city"] = city
        else:
            contact["city"] = None
        
        if area:
            area["_id"] = str(area["_id"])
            contact["area"] = area
        else:
            contact["area"] = None

    return [ContactOut(**contact) for contact in contacts]

async def deleteContact(contactId: str):
    result = await contact_collection.delete_one({"_id": ObjectId(contactId)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact Deleted Successfully"}
