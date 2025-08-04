from fastapi import FastAPI
from routers import expense, login, signup

app = FastAPI()

# Include all routers here
app.include_router(expense.router)
app.include_router(login.router)
app.include_router(login.router, prefix="/api")
app.include_router(signup.router, prefix="/api")  # ✅ This was missing!

@app.get("/")
def root():
    return {"status": "Backend is working"}
