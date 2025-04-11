from fastapi import APIRouter
from controllers.ContactController import addContact, getContacts, deleteContact
from models.ContactModel import Contact

router = APIRouter()

@router.post("/contact/")
async def post_contact(contact: Contact):
    return await addContact(contact)

@router.get("/contact/")
async def get_contact():
    return await getContacts()

@router.delete("/contact/{contactId}")
async def delete_contact(contactId: str):
    return await deleteContact(contactId)
