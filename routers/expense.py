from fastapi import APIRouter
from schemas.expense import ExpenseCreate, ExpenseOut
from services.expense_service import add_expense, get_expenses
from typing import List

router = APIRouter(prefix="/tools/expenses", tags=["expenses"])

@router.post("/", response_model=ExpenseOut)
def create_expense(expense: ExpenseCreate):
    return add_expense(expense)

@router.get("/{user_id}", response_model=List[ExpenseOut])
def list_expenses(user_id: str):
    return get_expenses(user_id)
