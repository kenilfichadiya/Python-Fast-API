import cloudinary
from cloudinary.uploader import upload

#cloundinary configuration
cloudinary.config(
    cloud_name = "diny7ds2h",
    api_key="133673658963774",
    api_secret="MPkgqH0lHNEPOhtjWdmgujXFzZo"
)

#util functionn...

async def upload_image(image):
    result = upload(image)
    print("cloundianry response,",result)
    return result["secure_url"] #string




# import cloudinary
# from cloudinary.uploader import upload
# import os

# # Load Cloudinary credentials from environment variables
# cloudinary.config(
#     cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
#     api_key=os.getenv("CLOUDINARY_API_KEY"),
#     api_secret=os.getenv("CLOUDINARY_API_SECRET"),
# )

# async def upload_image(image_path: str) -> str:
#     try:
#         result = upload(image_path)
#         print("Cloudinary response:", result)
#         return result.get("secure_url", "")  # Return secure URL or empty string if missing
#     except Exception as e:
#         print(f"Cloudinary Upload Error: {e}")
#         return ""  # Return empty string in case of failure
