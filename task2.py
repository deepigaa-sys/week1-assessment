# Task 2: Files, APIs and Environment
import csv
import json
import os
import requests
from dotenv import load_dotenv

# 1. Load environment variables from .env
load_dotenv()
API_KEY = os.getenv("API_KEY", "dummy_key")

# 2. Read employees.csv and write JSON outputs (employees.json and high_earners.json)
employees = []
high_earners = []

with open('employees.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        employees.append(row)
        if int(row['salary']) > 50000:
            high_earners.append(row)

with open('employees.json', 'w') as f:
    json.dump(employees, f, indent=4)

with open('high_earners.json', 'w') as f:
    json.dump(high_earners, f, indent=4)

print(f"Rows read: {len(employees)} | High earners: {len(high_earners)}")

# 3. API Call with timeout, status codes, error handling, and .get() parsing
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
    if response.status_code == 200:
        users = response.json()
        for user in users[:1]:
            user_id = user.get('id')
            name = user.get('name')
            email = user.get('email')
            print(f"{user_id} - {name} - {email}")
    
    # Handling 404 error endpoint (/users/9999)
    res_404 = requests.get("https://jsonplaceholder.typicode.com/users/9999", timeout=5)
    if res_404.status_code == 404:
        print("/users/9999 -> 404 Not found")
        
except (requests.Timeout, requests.ConnectionError):
    print("Connection or Timeout Error occurred")