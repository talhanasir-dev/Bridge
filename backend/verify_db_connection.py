import os
import pymongo
import certifi
from dotenv import load_dotenv

load_dotenv()

try:
    mongo_uri = os.getenv("MONGODB_URI")
    if not mongo_uri:
        print("MONGODB_URI not found in environment variables.")
    else:
        client = pymongo.MongoClient(
            mongo_uri,
            tlsCAFile=certifi.where(),
            serverSelectionTimeoutMS=5000
        )
        client.admin.command('ismaster')
        print("Successfully connected to the MongoDB database.")
except Exception as e:
    print(f"Failed to connect to the MongoDB database: {e}")