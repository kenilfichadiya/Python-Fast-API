
from fastapi import APIRouter
from controllers.ContactUsController import addCont,getCont,deleteCont
from models.ContactUsModel import ContactUs,ContactUsOut
from bson import ObjectId

router =APIRouter()

@router.post("/contact_us")
async def post_contact_us(cont:ContactUs):
    return await addCont(cont)

@router.get("/contact_us")
async def get_contact_us():
    return await getCont()

@router.delete("/contact_us/{contId}")
async def delete_contact_us(contId: str):
    return await deleteCont(contId)
