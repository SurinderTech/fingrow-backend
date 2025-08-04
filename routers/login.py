# routers/login.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_ANON_KEY")

supabase: Client = create_client(url, key)

router = APIRouter(
    prefix="/api",
    tags=["Login"]
)

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login_user(data: LoginRequest):
    try:
        res = supabase.auth.sign_in_with_password({
            "email": data.email,
            "password": data.password
        })

        if not res.session:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        return {
            "message": "Login successful",
            "user": res.user,
            "access_token": res.session.access_token,
            "refresh_token": res.session.refresh_token
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
