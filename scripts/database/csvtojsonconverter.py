import pandas as pd
from pymongo import MongoClient
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Function to convert CSV to JSON
def csv_to_json(csv_file):
    data = pd.read_csv(csv_file)
    return json.loads(data.to_json(orient='records'))

# Function to add a new field to each document
def add_new_field(documents):
    for document in documents:
        document['origin_website'] = 'Our World Data'
        document['origin_url'] = 'https://ourworldindata.org/coronavirus/country/brazil'
    return documents    

# MongoDB connection settings
mongodb_url = os.getenv("MONGODB_URL")
database_name = os.getenv("DATABASE_NAME")
collection_name = os.getenv("COLLECTION_NAME")

# Now you can use these variables in your script
# print("Database Host:", mongodb_url)
# print("Database Port:", database_name)
# print("Database Name:", db_name)

# Load CSV into JSON
csv_file_path = "../scripts/database/jsondata/owid-covid-data.csv"
json_data = csv_to_json(csv_file_path)

# Connect to MongoDB
client = MongoClient(mongodb_url)
db = client[database_name]
collection = db[collection_name]

# Add new field to each document
json_data_with_new_field = add_new_field(json_data)

# Insert JSON data into MongoDB collection
collection.insert_many(json_data)

print("Data inserted successfully into MongoDB.")

# Close MongoDB connection
client.close()


