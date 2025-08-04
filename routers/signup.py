# routers/signup.py
# routers/signup.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.supabase_client import supabase

router = APIRouter()

class SignUpData(BaseModel):
    email: str
    password: str

@router.post("/signup")
def signup(data: SignUpData):
    try:
        res = supabase.auth.sign_up({
            "email": data.email,
            "password": data.password
        })
        print("✅ Supabase response:", res)
        return {"message": "Signup successful", "data": res}
    except Exception as e:
        print("❌ Signup error:", e)  # 👈 Add this line to see full error in terminal
        raise HTTPException(status_code=500, detail=str(e))
