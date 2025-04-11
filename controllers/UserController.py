# from models.UserModel import User,UserOut,UserLogin
# from bson import ObjectId
# from config.database import user_collection,role_collection
# from fastapi import HTTPException
# from fastapi.responses import JSONResponse
# import bcrypt
# from models.UserModel import User


# async def addUser(user:User):
#     #typeCast
#     #print("user....",user.role_id)
#     #convert string id to object it comp.,, to mongo db
#     user.role_id = ObjectId(user.role_id)
#     print("after type cast",user.role_id)
#     result = await user_collection.insert_one(user.dict())
#     #return {"Message":"user created successfully"}
    
#     return JSONResponse(status_code=200,content={"message":"User created successfully"})
#     #raise HTTPException(status_code=500,detail="User not created")

# # async def getAllUsers():
# #     users = await user_collection.find().to_list()
# #     print("users",users)
# #     return [UserOut(**user) for user in users]

# async def getAllUsers():
#     users = await user_collection.find().to_list(length=None)

#     for user in users:
#         # Convert role_id from ObjectId to str before validation
#         if "role_id" in user and isinstance(user["role_id"], ObjectId):
#             user["role_id"] = str(user["role_id"])
        
#         # Fetch role details
#         role = await role_collection.find_one({"_id": ObjectId(user["role_id"])})  
        
#         if role:
#             role["_id"] = str(role["_id"])  # Convert role _id to string
#             user["role"] = role

#     return [UserOut(**user) for user in users]

# async def loginUser(request:UserLogin):
# #async def loginUser(email:str,password:str):
#     #norma; password : plain text --> encr
    
#     foundUser = await user_collection.find_one({"email":request.email})
#     print(":foundUser",foundUser)
    
#     foundUser["_id"] = str(foundUser["_id"])
#     foundUser["role_id"] = str(foundUser["role_id"])
    
#     if foundUser is None:
#         raise HTTPException(status_code=404,detail="User not found")
#     #compare password
#     if "password" in foundUser and bcrypt.checkpw(request.password.encode(),foundUser["password"].encode()):
#         #database role.. roleid
#         role = await role_collection.find_one({"_id":ObjectId(foundUser["role_id"])})
#         foundUser["role"] = role
#         return {"message":"user login success","user":UserOut(**foundUser)}
#     else:
#         raise HTTPException(status_code=404,detail="Invalid password")
    


# from models.UserModel import User,UserOut,UserLogin
# from bson import ObjectId
# from config.database import user_collection,role_collection
# from fastapi import HTTPException
# from fastapi.responses import JSONResponse
# import bcrypt
# from utils.SendMail import send_mail

# async def addUser(user:User):
#     #typeCast
#     #print("user....",user.role_id)
#     #convert string id to object it comp.,, to mongo db
#     user.role_id = ObjectId(user.role_id)
#     print("after type cast",user.role_id)
#     result = await user_collection.insert_one(user.dict())
#     send_mail(user.email,"User Created","User created successfully")
#     #mail...
#     #return {"Message":"user created successfully"}
    
#     return JSONResponse(status_code=201,content={"message":"User created successfully"})
#     #raise HTTPException(status_code=500,detail="User not created")

# # async def getAllUsers():
# #     users = await user_collection.find().to_list()
# #     print("users",users)
# #     return [UserOut(**user) for user in users]

# async def getAllUsers():
#     users = await user_collection.find().to_list(length=None)

#     for user in users:
#         # Convert role_id from ObjectId to str before validation
#         if "role_id" in user and isinstance(user["role_id"], ObjectId):
#             user["role_id"] = str(user["role_id"])
        
#         # Fetch role details
#         role = await role_collection.find_one({"_id": ObjectId(user["role_id"])})  
        
#         if role:
#             role["_id"] = str(role["_id"])  # Convert role _id to string
#             user["role"] = role

#     return [UserOut(**user) for user in users]

# async def loginUser(request:UserLogin):
# #async def loginUser(email:str,password:str):
#     #norma; password : plain text --> encr
    
#     foundUser = await user_collection.find_one({"email":request.email})
#     print(":foundUser",foundUser)
    
#     foundUser["_id"] = str(foundUser["_id"])
#     foundUser["role_id"] = str(foundUser["role_id"])
    
#     if foundUser is None:
#         raise HTTPException(status_code=404,detail="User not found")
#     #compare password
#     if "password" in foundUser and bcrypt.checkpw(request.password.encode(),foundUser["password"].encode()):
#         #database role.. roleid
#         role = await role_collection.find_one({"_id":ObjectId(foundUser["role_id"])})
#         foundUser["role"] = role
#         return {"message":"user login success","user":UserOut(**foundUser)}
#     else:
#         raise HTTPException(status_code=404,detail="Invalid password")
    
# async def deleteUser(userId:str):
#     result = await user_collection.delete_one({"_id":ObjectId(userId)})
#     print("after delete result",result)
#     return {"Message":"User Deleted Successfully!"}



# from models.UserModel import User, UserOut, UserLogin
# from bson import ObjectId
# from config.database import user_collection, role_collection
# from fastapi import HTTPException
# from fastapi.responses import JSONResponse
# import bcrypt
# from utils.SendMail import send_mail

# async def addUser(user: User):
#     try:
#         # Ensure valid ObjectId
#         if not ObjectId.is_valid(user.role_id):
#             raise HTTPException(status_code=400, detail="Invalid role ID")

#         # Convert string to ObjectId
#         user.role_id = ObjectId(user.role_id)
#         result = await user_collection.insert_one(user.dict())
#         send_mail(user.email, "User Created", "User created successfully")
#         return JSONResponse(status_code=201, content={"message": "User created successfully"})
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# async def getAllUsers():
#     users = await user_collection.find().to_list(length=None)

#     for user in users:
#         if "role_id" in user and isinstance(user["role_id"], ObjectId):
#             user["role_id"] = str(user["role_id"])
#             role = await role_collection.find_one({"_id": ObjectId(user["role_id"])});
#             if role:
#                 role["_id"] = str(role["_id"])
#                 user["role"] = role
#     return [UserOut(**user) for user in users]

# async def loginUser(request: UserLogin):
#     foundUser = await user_collection.find_one({"email": request.email})

#     if not foundUser:
#         raise HTTPException(status_code=404, detail="User not found")

#     foundUser["_id"] = str(foundUser["_id"])
#     foundUser["role_id"] = str(foundUser["role_id"])

#     # Validate password
#     if "password" in foundUser and bcrypt.checkpw(request.password.encode(), foundUser["password"].encode()):
#         role = await role_collection.find_one({"_id": ObjectId(foundUser["role_id"])});
#         foundUser["role"] = role
#         return {"message": "User login success", "user": UserOut(**foundUser)}
#     else:
#         raise HTTPException(status_code=401, detail="Invalid password")

# async def deleteUser(userId: str):
#     if not ObjectId.is_valid(userId):
#         raise HTTPException(status_code=400, detail="Invalid user ID")
#     result = await user_collection.delete_one({"_id": ObjectId(userId)})
#     return {"Message": "User Deleted Successfully!"}



# from models.UserModel import User, UserOut, UserLogin
# from bson import ObjectId
# from config.database import user_collection, role_collection
# from fastapi import HTTPException
# from fastapi.responses import JSONResponse
# import bcrypt
# from utils.SendMail import SendMail

# async def addUser(user: User):
#     try:
#         if not ObjectId.is_valid(user.role_id):
#             raise HTTPException(status_code=400, detail="Invalid role ID")
#         role_id = ObjectId(user.role_id)

#         user_data = user.dict()
#         user_data["role_id"] = role_id
#         result = await user_collection.insert_one(user_data)
#         SendMail(user.email,"User Created","User Created Successfullly")

#         try:
#             SendMail(user.email, "Welcome to PocketBuddy!", "User created successfully")
#         except Exception as e:
#             print(f"Email failed to send: {str(e)}")
#             return JSONResponse(status_code=500, content={"message": "User created but email failed to send."})

#         return JSONResponse(status_code=201, content={"message": "User created successfully"})
#     except Exception as e:
#         print(f"Error in addUser: {str(e)}")
#         raise HTTPException(status_code=500, detail=str(e))

# async def getAllUsers():
#     try:
#         users = await user_collection.find().to_list(length=None)
#         for user in users:
#             if "role_id" in user and isinstance(user["role_id"], ObjectId):
#                 user["role_id"] = str(user["role_id"])
#                 role = await role_collection.find_one({"_id": ObjectId(user["role_id"])});
#                 if role:
#                     role["_id"] = str(role["_id"])
#                     user["role"] = role
#         return [UserOut(**user) for user in users]
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# async def loginUser(request: UserLogin):
#     try:
#         foundUser = await user_collection.find_one({"email": request.email})
#         if not foundUser:
#             raise HTTPException(status_code=404, detail="User not found")

#         foundUser["_id"] = str(foundUser["_id"])
#         foundUser["role_id"] = str(foundUser["role_id"])

#         # Validate password
#         if "password" in foundUser and bcrypt.checkpw(request.password.encode(), foundUser["password"].encode()):
#             role = await role_collection.find_one({"_id": ObjectId(foundUser["role_id"])});
#             if role:
#                 role["_id"] = str(role["_id"])
#                 foundUser["role"] = role
#             return {"message": "User login success", "user": UserOut(**foundUser)}
#         else:
#             raise HTTPException(status_code=401, detail="Invalid password")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# async def deleteUser(userId: str):
#     try:
#         if not ObjectId.is_valid(userId):
#             raise HTTPException(status_code=400, detail="Invalid user ID")
#         result = await user_collection.delete_one({"_id": ObjectId(userId)})
#         if result.deleted_count == 0:
#             raise HTTPException(status_code=404, detail="User not found")
#         return {"message": "User Deleted Successfully!"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))







from models.UserModel import User, UserOut, UserLogin,ResetPasswordReq
from config.database import user_collection
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import bcrypt
from utils.SendMail import SendMail
from bson import ObjectId
from datetime import datetime
import datetime
import jwt
import os

async def addUser(user: User):
    try:
        user_data = user.dict()
        result = await user_collection.insert_one(user_data)
        SendMail(user.email, "User Created", "User Created Successfully")

        try:
            SendMail(user.email, "Welcome to PocketBuddy!", "User created successfully")
        except Exception as e:
            print(f"Email failed to send: {str(e)}")
            return JSONResponse(status_code=500, content={"message": "User created but email failed to send."})

        return JSONResponse(status_code=201, content={"message": "User created successfully"})
    except Exception as e:
        print(f"Error in addUser: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

async def getAllUsers():
    try:
        users = await user_collection.find().to_list(length=None)
        return [UserOut(**user) for user in users]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def loginUser(request: UserLogin):
    try:
        foundUser = await user_collection.find_one({"email": request.email})
        if not foundUser:
            raise HTTPException(status_code=404, detail="User not found")

        foundUser["_id"] = str(foundUser["_id"])

        if "password" in foundUser and bcrypt.checkpw(request.password.encode(), foundUser["password"].encode()):
            return {"message": "User login success", "user": UserOut(**foundUser)}
        else:
            raise HTTPException(status_code=401, detail="Invalid password")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def deleteUser(userId: str):
    try:
        if not ObjectId.is_valid(userId):
            raise HTTPException(status_code=400, detail="Invalid user ID")
        result = await user_collection.delete_one({"_id": ObjectId(userId)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User Deleted Successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
SECRET_KEY ="royal"
def generate_token(email:str):
    expiration = datetime.datetime.utcnow()+datetime.timedelta(hours=1)
    payload = {"sub":email,"exp":expiration}
    token = jwt.encode(payload,SECRET_KEY,algorithm="HS256")
    return token


async def forgotPassword(email:str):
    foundUser = await user_collection.find_one({"email":email})
    if not foundUser:
        raise HTTPException(status_code=404,detail="email not found")
    
    token = generate_token(email)
    resetLink = f"http://localhost:5173/resetpassword/{token}"
    body = f"""
    <html>
        <h1>HELLO THIS IS RESET PASSWORD LINK EXPIRES IN 1 hour</h1>
        <a href= "{resetLink}">RESET PASSWORD</a>
    </html>
    """
    subject = "RESET PASSWORD"
    SendMail(email,subject,body)
    return {"message":"reset link sent successfully"}
    

async def resetPassword(data: ResetPasswordReq):
    try:
        payload = jwt.decode(data.token, SECRET_KEY, algorithms="HS256")
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=421, detail="Token is not valid...")

        # Hash the new password and decode the result to store it as a string
        hashed_password = bcrypt.hashpw(data.password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        await user_collection.update_one({"email": email}, {"$set": {"password": hashed_password}})

        return {"message": "Password updated successfully"}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=500, detail="JWT is expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=500, detail="JWT is invalid")

