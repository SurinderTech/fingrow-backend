from .supabase_client import supabase
from schemas.expense import ExpenseCreate

def add_expense(data: ExpenseCreate):
    response = supabase.table("expenses").insert(data.dict()).execute()
    return response.data

def get_expenses(user_id: str):
    response = supabase.table("expenses").select("*").eq("user_id", user_id).execute()
    return response.data
