# Lead Research & Scoring Agent - Roadmap & Checklist

## 🚀 Project Overview

This project is an AI-driven lead research and scoring agent that:

- Researches leads & companies
- Scores leads based on predefined rules
- Finds decision makers
- Fetches company location (longitude, latitude)
- Generates a personalized call script
- Updates a database with all lead data 
-

## 📂 Project Structure

```

lead-research-agent/
│── src/
│   ├── main.py                 # Main entry point
│   ├── research.py             # Fetching company & lead data
│   ├── scoring.py              # Lead scoring logic
│   ├── database.py             # Supabase integration
│   ├── decision_maker.py       # Finding decision makers
│   ├── call_script.py          # Generating personalized call scripts
│   ├── telegram_bot.py         # Telegram bot for user interaction
│   ├── utils.py                # Helper functions
│
│── config/
│   ├── settings.py             # API keys and configurations
│
│── tests/
│   ├── test_research.py        # Tests for research module
│   ├── test_scoring.py         # Tests for scoring module
│   ├── test_database.py        # Tests for database operations
│
│── README.md                   # Project documentation
│── requirements.txt             # Dependencies
│── .env                         # Environment variables

```

### **1️⃣ Setup & Core Configuration**
````
cd your-repository

git clone https://github.com/your-username/your-repository.git
````

### **2️⃣ Supabase Database Integration**
https://supabase.com/docs/reference/python/introduction

#### Installing
````
pip install supabase
````
#### Initializing
````
import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
````

You can initialize a new Supabase client using the create_client() method.

The Supabase client is your entrypoint to the rest of the Supabase functionality and is the easiest way to interact with everything offered within the Supabase ecosystem.

The unique Supabase URL which is supplied when you create a new project in your project dashboard.

The unique Supabase Key which is supplied when you create a new project in your project dashboard.

To test the connection go to "supabase → SQL Editor" and run this to create a table with these columbs 
````
CREATE TABLE leads (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    company TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
````
Run this test script to insert a test lead into the database to ensure proper functionality
````
test_lead = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "company": "TestCorp",
}

try:
    response = supabase.table("leads").insert(test_lead).execute()
    print("Successfully inserted test lead!")
    print(response)
except Exception as e:
    print("Failed to insert test lead:", e)
````
If the insert was successfull, the setup is completed and tested.

### **3️⃣ Lead Research Module**

-

### **3️⃣ Lead Scoring System**

-

### **5️⃣ Call Script Generator**

-

### **6️⃣ User Interface (Telegram Bot)**

-

### **7️⃣ Testing & Deployment**

-


