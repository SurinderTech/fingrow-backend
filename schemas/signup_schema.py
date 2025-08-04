from pydantic import BaseModel, EmailStr

class SignupSchema(BaseModel):
    name: str
    age: int
    income: float
    email: EmailStr
    password: str
