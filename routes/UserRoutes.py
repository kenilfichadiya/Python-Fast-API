# from fastapi import APIRouter,HTTPException
# from controllers.UserController import addUser,getAllUsers,loginUser
# from models.UserModel import User,UserOut,UserLogin
# from pydantic import BaseModel
# router = APIRouter()

# @router.post("/user/")
# async def post_user(user:User):
#     return await addUser(user)

# @router.get("/users/")
# async def get_users():
#     return await getAllUsers()

# @router.post("/user/login/")
# async def login_user(user:UserLogin):
#     return await loginUser(user)

# @router.post("/user")
# async def create_user(user: User):
#     return {"message": "User created successfully", "data": user}




# from fastapi import APIRouter, HTTPException
# from controllers.UserController import addUser, getAllUsers, loginUser,deleteUser
# from models.UserModel import User, UserOut, UserLogin

# router = APIRouter()

# @router.post("/user/")
# async def post_user(user: User):
#     return await addUser(user)

# @router.get("/users/")
# async def get_users():
#     return await getAllUsers()

# @router.post("/user/login/")
# async def login_user(user: UserLogin):
#     return await loginUser(user)


# @router.delete("/user/{userId}")
# async def delete_user(userId:str):
#     return await deleteUser(userId)




# from fastapi import APIRouter, HTTPException, Depends
# from controllers.UserController import addUser, getAllUsers, loginUser, deleteUser
# from models.UserModel import User, UserOut, UserLogin

# router = APIRouter()

# @router.post("/users", response_model=UserOut)
# async def post_user(user: User):
#     try:
#         return await addUser(user)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @router.get("/users", response_model=list[UserOut])
# async def get_users():
#     try:
#         return await getAllUsers()
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @router.post("/users/login", response_model=UserOut)
# async def login_user(user: UserLogin):
#     response = await loginUser(user)
#     if not response:
#         raise HTTPException(status_code=401, detail="Invalid email or password")
#     return response

# @router.delete("/users/{userId}")
# async def delete_user(userId: str):
#     try:
#         result = await deleteUser(userId)
#         if not result:
#             raise HTTPException(status_code=404, detail="User not found")
#         return {"message": "User deleted successfully"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))



# from fastapi import APIRouter, HTTPException
# from controllers.UserController import addUser, getAllUsers, loginUser, deleteUser
# from models.UserModel import User, UserOut, UserLogin

# router = APIRouter()

# @router.post("/user/")
# async def post_user(user: User):
#     try :
#         return await addUser(user)
#     except Exception as e :
#         raise HTTPException(status_code=400, detail=str(e))
    

# @router.get("/user/")
# async def get_users():
#     try :
#         return await getAllUsers()
#     except Exception as e :
#         raise HTTPException(status_code=500, detail=str(e))
    

# @router.post("/user/login/")
# async def login_user(user: UserLogin):
#     try :
#         return await loginUser(user)
#     except Exception as e :
#         raise HTTPException(status_code=401, detail="Invalid credentials")
    

# @router.delete("/user/{userId}")
# async def delete_user(userId: str):
#     try :
#         return await deleteUser(userId)
#     except Exception as e :
#         raise HTTPException(status_code=404, detail=str(e))
    




from fastapi import APIRouter, HTTPException
from controllers.UserController import addUser, getAllUsers, loginUser, deleteUser,forgotPassword,resetPassword
from models.UserModel import User, UserOut, UserLogin,ResetPasswordReq

router = APIRouter()

@router.post("/user/")
async def post_user(user: User):
    try:
        return await addUser(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/user/")
async def get_users():
    try:
        return await getAllUsers()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/user/login/")
async def login_user(user: UserLogin):
    try:
        return await loginUser(user)
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@router.delete("/user/{userId}")
async def delete_user(userId: str):
    try:
        return await deleteUser(userId)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.post("/forgotpassword")
async def forgot_password(email:str):
    return await forgotPassword(email)

@router.post("/resetpassword")
async def reset_password(data:ResetPasswordReq):
    return await resetPassword(data)