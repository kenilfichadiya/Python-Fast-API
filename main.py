# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# # Import route modules
# from routes.RoleRoutes import router as role_router
# from routes.UserRoutes import router as user_router
# from routes.DepartmentRoutes import router as department_router
# from routes.EmployeeRoutes import router as employee_router
# from routes.StateRoutes import router as state_router
# from routes.CityRoutes import router as city_router
# from routes.AreaRoutes import router as area_router
# from routes.LocationRoutes import router as location_router
# from routes.OfferRoutes import router as offer_router  
# from routes.RatingRoutes import router as rating_router

# # Initialize FastAPI app
# app = FastAPI()



# # # Define allowed origins (frontend URL)
# # origins = [
# #     "http://localhost:5175",  # Your React frontend
# #     "http://127.0.0.1:5175",
# #     "http://localhost:3000",  # If you're using a different port
# #     "*",  # (Temporary) Allow all origins - NOT recommended for production
# # ]



# # Configure CORS Middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  
#     allow_credentials=True,
#     allow_methods=["*"],  
#     allow_headers=["*"],  
# )



# # Root route for testing
# @app.get("/")
# async def root():
#     return {"message": "Backend is running"}



# # Include all routers
# app.include_router(role_router)
# app.include_router(user_router)
# app.include_router(department_router)
# app.include_router(employee_router)
# app.include_router(state_router)
# app.include_router(city_router)
# app.include_router(area_router)
# app.include_router(location_router)
# app.include_router(offer_router)  
# app.include_router(rating_router)

# # Run FastAPI Server
# if __name__ == "__main__":
#     import uvicorn  
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)



# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from routes.UserRoutes import router as user_router
# from routes.RoleRoutes import router as role_router
# from routes.DepartmentRoutes import router as department_router
# from routes.EmployeeRoutes import router as employee_router
# from routes.StateRoutes import router as state_router
# from routes.CityRoutes import router as city_router
# from routes.AreaRoutes import router as area_router
# from routes.LocationRoutes import router as location_router
# from routes.OfferRoutes import router as offer_router
# from routes.RatingRoutes import router as rating_router

# app = FastAPI()

# # CORS Configuration
# origins = [
#     "http://localhost:5173",
#     "http://127.0.0.1:5173",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Test Route
# @app.get("/")
# async def root():
#     return {"message": "Backend is running"}

# # Include Routers with Prefix
# app.include_router(user_router, prefix="/api")
# app.include_router(role_router, prefix="/api")
# app.include_router(department_router, prefix="/api")
# app.include_router(employee_router, prefix="/api")
# app.include_router(state_router, prefix="/api")
# app.include_router(city_router, prefix="/api")
# app.include_router(area_router, prefix="/api")
# app.include_router(location_router, prefix="/api")
# app.include_router(offer_router, prefix="/api")
# app.include_router(rating_router, prefix="/api")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)




# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from routes.UserRoutes import router as user_router
# from routes.RoleRoutes import router as role_router
# from routes.DepartmentRoutes import router as department_router
# from routes.EmployeeRoutes import router as employee_router
# from routes.StateRoutes import router as state_router
# from routes.CityRoutes import router as city_router
# from routes.AreaRoutes import router as area_router
# from routes.LocationRoutes import router as location_router
# from routes.OfferRoutes import router as offer_router
# from routes.RatingRoutes import router as rating_router


# app = FastAPI()

# # Fix CORS Configuration
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allow all origins (for testing purposes)
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, etc.)
#     allow_headers=["*"],  # Allow all headers
# )

# # Root route for testing
# # @app.get("/")
# # async def root():
# #     return {"message": "Backend is running"}

# # Include API routers with the '/api' prefix
# # app.include_router(user_router, prefix="/api")
# # app.include_router(role_router, prefix="/api")
# # app.include_router(department_router, prefix="/api")
# # app.include_router(employee_router, prefix="/api")
# # app.include_router(state_router, prefix="/api")
# # app.include_router(city_router, prefix="/api")
# # app.include_router(area_router, prefix="/api")
# # app.include_router(location_router, prefix="/api")
# # app.include_router(offer_router, prefix="/api")
# # app.include_router(rating_router, prefix="/api")


# app.include_router(user_router)
# app.include_router(role_router)
# app.include_router(department_router)
# app.include_router(employee_router)
# app.include_router(state_router)
# app.include_router(city_router)
# app.include_router(area_router)
# app.include_router(location_router)
# app.include_router(offer_router)
# app.include_router(rating_router)


# # if __name__ == "__main__":
# #     import uvicorn
# #     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# import warnings
# warnings.filterwarnings("ignore", category=UserWarning)




from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.UserRoutes import router as user_router
from routes.RoleRoutes import router as role_router
from routes.DepartmentRoutes import router as department_router
from routes.EmployeeRoutes import router as employee_router
from routes.StateRoutes import router as state_router
from routes.CityRoutes import router as city_router
from routes.AreaRoutes import router as area_router
from routes.LocationRoutes import router as location_router
from routes.OfferRoutes import router as offer_router
from routes.RatingRoutes import router as rating_router
from routes.ContactRoutes import router as contact_router
from routes.ContactUsRoutes import router as contactus_router


app = FastAPI()


# CORS Configuration (Allow Frontend Ports)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route for testing
@app.get("/")
async def root():
    return {"message": "Backend is running"}


# Include API routers without prefix
app.include_router(user_router)
app.include_router(role_router)
app.include_router(department_router)
app.include_router(employee_router)
app.include_router(state_router)
app.include_router(city_router)
app.include_router(area_router)
app.include_router(location_router)
app.include_router(offer_router)
app.include_router(rating_router)
app.include_router(contact_router)
app.include_router(contactus_router)


# Run the server using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
