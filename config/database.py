from motor.motor_asyncio import AsyncIOMotorClient

# DB Connection
MONGO_URL = "mongodb://localhost:27017"
DATABASE_NAME = "25_internship_fast"

client = AsyncIOMotorClient(MONGO_URL)
db = client[DATABASE_NAME]

# Collections
role_collection = db["roles"]
user_collection = db["users"]
department_collection = db["departments"]
employee_collection = db["employees"]
state_collection = db["states"]
city_collection = db["cities"]
area_collection = db["areas"]
location_collection = db["locations"]
offer_collection = db["offers"]  
rating_collection = db["ratings"]
contact_collection=db["contact"]
contactus_collection=db["contactus"]



