# supabase.py
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

# Match these exactly with your .env variable names
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE = os.getenv("SUPABASE_SERVICE_ROLE")

# Ensure values are loaded correctly
if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE:
    raise Exception("Supabase credentials not found. Check your .env file and variable names.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE)
