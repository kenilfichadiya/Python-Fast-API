from models.ContactUsModel import ContactUs,ContactUsOut
from bson import ObjectId
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException
from config.database import contactus_collection

async def addCont(cont:ContactUs):
    savedCont= await contactus_collection.insert_one(cont.dict())
    return JSONResponse(content={"message":"Added successfully"},status_code=201)

async def getCont():
    conts = await contactus_collection.find().to_list()
    if len(conts) == 0:
        return JSONResponse(status_code=404,content={"message":"No states Found"})
    
    return [ContactUsOut(**cont) for cont in conts]

async def deleteCont(contId:str):
    result = await contactus_collection.delete_one({"_id":ObjectId(contId)})
    print("after delete result",result)
    if result.deleted_count == 1:
        return JSONResponse(status_code=200,content={"message":"Contact us deleted successfully"})
    else:
        raise HTTPException(status_code=404,detail="Contact us not found")
