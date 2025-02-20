import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

supabase_url: str = os.environ.get("SUPABASE_URL")
supabase_key: str = os.environ.get("SUPABASE_KEY")

#initialize Supabase client
supabase: Client = create_client(supabase_url, supabase_key)

# Connection test to Supabase
try:
    response = supabase.auth.get_user()
    print("Supabase connection is working!")
    print(response)
except Exception as e:
    print("Supabase connection failed:", e)



# Function to insert leads into the "leads" table
def insert_lead(name:str, email:str, number:int, company:str):

#Check if the required fields are missing
    if not name or not email or not number or not company:
        print("Missing required fields (name, email, number, company).")
        return None
	
    leads = {"name": name, "email": email, "number": number, "company": company}

#Check if the lead was successfully inserted into the "leads" table
    try:
        response = supabase.table("leads").insert(leads).execute()
        print(f"Successfully inserted lead: {name}")
        return response
    except Exception as e:
        print(f"Failed to insert lead: {name}", e)
        return None



# Function to fetch all leads from the "leads" table
def fetch_all_leads():
    try:
        response = supabase.table("leads").select("*").execute()
        return response.data
    except Exception as e:
        print("Failed to fetch leads:", e)
        return None



# Create separate functions to fetch, update and delete leads by id name, email, number and company

#Fetch by id
def fetch_id_leads(id: int):
	try:
		response = supabase.table("leads").select("*").eq("id", id).execute()
		return response.data
	except Exception as e:
		print("Failed to fetch leads by id:", e)
		return None

#Update by id
def update_id_leads(id: int, name: str, email: str, number: int, company: str):
	leads = {"name": name, "email": email, "number": number, "company": company}
	try:
		response = supabase.table("leads").update(leads).eq("id", id).execute()
		return response.data
	except Exception as e:
		print("Failed to update leads by id:", e)
		return None

#Delete by id
def delete_id_leads(id: int):
	try:
		response = supabase.table("leads").delete().eq("id", id).execute()
		return response.data
	except Exception as e:
		print("Failed to delete leads by id:", e)
		return None



#Fetch by name
def fetch_name_leads(name: str):
    try:
        response = supabase.table("leads").select("*").eq("name", name).execute()
        return response.data
    except Exception as e:
        print("Failed to fetch leads by name:", e)
        return None

#Update by name
def update_name_leads(name: str, email: str, number: int, company: str):
	leads = {"email": email, "number": number, "company": company}
	try:
		response = supabase.table("leads").update(leads).eq("name", name).execute()
		return response.data
	except Exception as e:
		print("Failed to update leads by name:", e)
		return None

#Delete by name
def delete_name_leads(name: str):
	try:
		response = supabase.table("leads").delete().eq("name", name).execute()
		return response.data
	except Exception as e:
		print("Failed to delete leads by name:", e)
		return None



#Fetch by email
def fetch_email_leads(email: str):
	try:
		response = supabase.table("leads").select("*").eq("email", email).execute()
		return response.data
	except Exception as e:
		print("Failed to fetch leads by email:", e)
		return None

#update by email
def update_email_leads(email: str, number: int, company: str):
	leads = {"number": number, "company": company}
	try:
		response = supabase.table("leads").update(leads).eq("email", email).execute()
		return response.data
	except Exception as e:
		print("Failed to update leads by email:", e)
		return None

#Delete by email
def delete_email_leads(email: str):
	try:
		response = supabase.table("leads").delete().eq("email", email).execute()
		return response.data
	except Exception as e:
		print("Failed to delete leads by email:", e)
		return None



#Fetch by number
def fetch_number_leads(number: int):
	try:
		response = supabase.table("leads").select("*").eq("number", number).execute()
		return response.data
	except Exception as e:
		print("Failed to fetch leads by number:", e)
		return None

#Update by number
def update_number_leads(number: int, name: str, email: str, company: str):
	leads = {"name": name, "email": email, "company": company}
	try:
		response = supabase.table("leads").update(leads).eq("number", number).execute()
		return response.data
	except Exception as e:
		print("Failed to update leads by number:", e)
		return None

#delete by number
def delete_number_leads(number: int):
	try:
		response = supabase.table("leads").delete().eq("number", number).execute()
		return response.data
	except Exception as e:
		print("Failed to delete leads by number:", e)
		return None



#Fetch by company
def fetch_company_leads(company: str):
	try:
		response = supabase.table("leads").select("*").eq("company", company).execute()
		return response.data
	except Exception as e:
		print("Failed to fetch leads by company:", e)
		return None

#Update by company
def update_company_leads(company: str, name: str, email: str, number: int):
	leads = {"name": name, "email": email, "number": number}
	try:
		response = supabase.table("leads").update(leads).eq("company", company).execute()
		return response.data
	except Exception as e:
		print("Failed to update leads by company:", e)
		return None

#Delete by company
def delete_company_leads(company: str):
	try:
		response = supabase.table("leads").delete().eq("company", company).execute()
		return response.data
	except Exception as e:
		print("Failed to delete leads by company:", e)
		return None