# All of the code in this file is used to test the connection to the Supabase database. 
# The code first initializes the Supabase client using the Supabase URL and key from the environment variables. 


from dotenv import load_dotenv
import os
from supabase import create_client, Client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

#initialize Supabase client
supabase: Client = create_client(url, key)

#Remove this code block later
try:
    response = supabase.auth.get_user()
    print("Supabase connection is working!")
    print(response)
except Exception as e:
    print("Supabase connection failed:", e)
    
    
# Testing the connection to the database by inserting a test lead
test_lead = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "company": "TestCorp",
}

# Insert test lead into the "leads" table
try:
    response = supabase.table("leads").insert(test_lead).execute()
    print("Successfully inserted test lead!")
    print(response)
except Exception as e:
    print("Failed to insert test lead:", e)