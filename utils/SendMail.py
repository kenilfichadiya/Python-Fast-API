from fastapi import FastAPI
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_EMAIL ="kenilfichadiya79@gmail.com"
SMTP_PASSWORD="eyae hwgx wxow jesi"

def SendMail(to_email:str,subject:str,text:str):
    msg = MIMEMultipart()
    msg['From'] = SMTP_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(text,'html'))
    
    #connect to mail server....
    server = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
    server.starttls()
    server.login(SMTP_EMAIL,SMTP_PASSWORD)
    server.sendmail(SMTP_EMAIL,to_email,msg.as_string())
    server.quit()
    
    return {"message":"Mail sent successfully"}

#send_mail("samir.vithlani83955@gmail.com","Test Mail","This is a test mail from fast...")


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# app = FastAPI()

# # Allow frontend to access backend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],  # React dev server
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Email configuration
# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 587
# SMTP_EMAIL = "kenilfichadiya79@gmail.com"
# SMTP_PASSWORD = "eyae hwgx wxow jesi"  # Consider using .env for security

# # Utility to send email
# def SendMail(to_email: str, subject: str, text: str):
#     msg = MIMEMultipart()
#     msg['From'] = SMTP_EMAIL
#     msg['To'] = to_email
#     msg['Subject'] = subject
#     msg.attach(MIMEText(text, 'html'))

#     server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#     server.starttls()
#     server.login(SMTP_EMAIL, SMTP_PASSWORD)
#     server.sendmail(SMTP_EMAIL, to_email, msg.as_string())
#     server.quit()

#     return {"message": "Mail sent successfully"}

# # Pydantic model for request body
# class ContactForm(BaseModel):
#     name: str
#     email: str
#     message: str

# # Route to send email
# @app.post("/contact/")
# async def send_contact_email(contact: ContactForm):
#     name = contact.name
#     email = contact.email
#     message = contact.message

#     # Sending email to yourself
#     SendMail(
#         SMTP_EMAIL,
#         f"New message from {name}",
#         f"Name: {name}<br>Email: {email}<br>Message: {message}"
#     )

#     return {"message": "Message sent successfully!"}
