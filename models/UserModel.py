# from pydantic import BaseModel,Field,validator
# from bson import ObjectId
# from typing import Optional, Dict, Any
# import bcrypt   #pip install bcrypt



# class User(BaseModel):
#     firstName:str
#     lastName:str
#     age:int
#     status:bool
#     role_id:str
#     email:str
#     password:str
    
#     #10,11,12,13,14,15,16,20,,,25,31
#     @validator("password",pre=True,always=True)
#     def encrypt_password(cls,v):
#         if v is None:
#             return None
#         return bcrypt.hashpw(v.encode("utf-8"),bcrypt.gensalt())
        
    
#     # @validator("role_id",pre=True,always=True)
#     # def convert_objectId(cls,v):
#     #     if isinstance(v,ObjectId):
#     #         return str(v)
#     #     return v


# class UserOut(BaseModel):
#     id:str = Field(alias="_id")    
#     #role:str = Field(alias="role_id")
#     #[{firstna,,,,role:{"onjectid",des,name}},{},{}]
#     role:Optional[Dict[str,Any]] = None
#     email:Optional[str] = None
#     password:Optional[str] = None
    
#     @validator("id",pre=True,always=True)
#     def convert_objectId(cls,v):
#         if isinstance(v,ObjectId):
#             return str(v)
#         return v
    
#     @validator("role", pre=True, always=True)
#     def convert_role(cls, v):
#         if isinstance(v, dict) and "_id" in v:
#             v["_id"] = str(v["_id"])  # Convert role _id to string
#         return v
    
# class UserLogin(BaseModel):
#     email:str
#     password:str    


# from pydantic import BaseModel, Field, validator, EmailStr
# from bson import ObjectId
# from typing import Optional, Dict, Any
# import bcrypt  # Ensure bcrypt is installed: pip install bcrypt

# class User(BaseModel):
#     firstName: str
#     lastName: str
#     age: int
#     status: bool
#     role_id: str
#     email: EmailStr
#     password: str

#     @validator("password", pre=True, always=True)
#     def encrypt_password(cls, v):
#         if v is None:
#             return None
#         return bcrypt.hashpw(v.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")  # Ensure it returns a string
    

#     # @validator("role_id", pre=True, always=True)
#     # def convert_objectId(cls, v):
#     #     if isinstance(v, ObjectId):
#     #         return str(v)
#     #     return v

# class UserOut(BaseModel):
#     firstName:Optional[str] = None
#     lastName:Optional[str] =None
#     age:Optional[int] = None
#     id: str = Field(alias="_id")
#     role: Optional[Dict[str, Any]] = None
#     email: Optional[str] = None
#     password: Optional[str] = None

#     @validator("id", pre=True, always=True)
#     def convert_objectId(cls, v):
#         if isinstance(v, ObjectId):
#             return str(v)
#         return v

#     @validator("role", pre=True, always=True)
#     def convert_role(cls, v):
#         if isinstance(v, dict) and "_id" in v:
#             v["_id"] = str(v["_id"])  # Convert role _id to string
#         return v

# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str




# from pydantic import BaseModel, Field, validator, EmailStr
# from bson import ObjectId
# from typing import Optional, Dict, Any
# import bcrypt

# class User(BaseModel):
#     firstName: str
#     lastName: str
#     age: int
#     status: bool  # Ensure status is a boolean
#     role_id: str
#     email: EmailStr
#     password: str

#     @validator("password", pre=True, always=True)
#     def encrypt_password(cls, v):
#         if v is None:
#             return None
#         return bcrypt.hashpw(v.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

# class UserOut(BaseModel):
#     firstName: Optional[str] = None
#     lastName: Optional[str] = None
#     age: Optional[int] = None
#     id: str = Field(alias="_id")
#     role: Optional[Dict[str, Any]] = None
#     email: Optional[str] = None
#     password: Optional[str] = None

#     @validator("id", pre=True, always=True)
#     def convert_objectId(cls, v):
#         if isinstance(v, ObjectId):
#             return str(v)
#         return v

#     @validator("role", pre=True, always=True)
#     def convert_role(cls, v):
#         if isinstance(v, dict) and "_id" in v:
#             v["_id"] = str(v["_id"])
#         return v

# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str




from pydantic import BaseModel, Field, validator, EmailStr
from bson import ObjectId
from typing import Optional, Dict, Any
import bcrypt

class User(BaseModel):
    firstName: str
    lastName: str
    age: int
    role: str
    email: EmailStr
    password: str

    @validator("password", pre=True, always=True)
    def encrypt_password(cls, v):
        if v is None:
            return None
        return bcrypt.hashpw(v.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

class UserOut(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    age: Optional[int] = None
    id: str = Field(alias="_id")
    role: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

    @validator("id", pre=True, always=True)
    def convert_objectId(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return v

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class ResetPasswordReq(BaseModel):
    token:str
    password:str 