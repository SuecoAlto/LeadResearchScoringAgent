import database as database

def main():
	print("Starting Lead Agent...")


test_lead = {
    "name": "John Doe",
    "email": "johndoe@example.com",
	"number": 1234567890,
    "company": "TestCorp",
}

insert_data = database.insert_lead(**test_lead)
print("\nInserted", insert_data)

respond_all_data = database.fetch_all_leads()


all_leads = database.fetch_all_leads()
print("\nAll leads in database:", all_leads)

email_to_update = "johndoe@example.com"
update_resp = database.update_email_leads(email_to_update, number=1234567891, company="NewCorp")
print("\nUpdate lead response:", update_resp)

# 4) Hämta leads efter uppdatering
updated_leads = database.fetch_email_leads(email_to_update)
print("\nUpdated lead info:", updated_leads)

# 5) Demonstrera borttagning
delete_resp = database.delete_email_leads(email_to_update)
print("\nDelete lead response:", delete_resp)

# 6) Hämta alla leads igen
all_leads_after_delete = database.fetch_all_leads()
print("\n\nAll leads after delete:", all_leads_after_delete)

if __name__ == "__main__":
    main()