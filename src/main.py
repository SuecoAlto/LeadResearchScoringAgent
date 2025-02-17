from dotenv import load_dotenv
import os
from supabase import create_client, Client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

#initialize Supabase client
supabase: Client = create_client(url, key)

#Remove this code block 
try:
    response = supabase.auth.get_user()
    print("Supabase connection is working!")
    print(response)
except Exception as e:
    print("Supabase connection failed:", e)
    
