from pydantic import BaseModel
from typing import Optional

class ExpenseCreate(BaseModel):
    user_id: str
    amount: float
    category: str
    date: str

class ExpenseOut(ExpenseCreate):
    id: Optional[int]
