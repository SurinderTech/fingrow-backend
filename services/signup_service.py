from supabase_client import supabase

def signup_user(email: str, password: str):
    try:
        result = supabase.auth.sign_up({
            "email": email,
            "password": password
        })
        return result
    except Exception as e:
        return {"error": str(e)}
