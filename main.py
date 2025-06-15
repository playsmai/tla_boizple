from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

email_code_db = {}

class EmailRequest(BaseModel):
    email: EmailStr

class CodeVerificationRequest(BaseModel):
    email: EmailStr
    code: str

@app.post("/send-code")
async def send_code(request: EmailRequest):
    code = f"{random.randint(10000, 99999)}"
    email_code_db[request.email] = code
    print(f"Simulated sending code {code} to {request.email}")
    return {"message": "Verification code sent."}

@app.post("/verify-code")
async def verify_code(request: CodeVerificationRequest):
    correct_code = email_code_db.get(request.email)
    if correct_code == request.code:
        alias = f"user{random.randint(1000, 9999)}@plaboi.st"
        return {"alias": alias}
    return JSONResponse(status_code=400, content={"error": "Invalid code"})