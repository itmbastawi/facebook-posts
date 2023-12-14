from pymongo import MongoClient
import os

# Function to connect to DocumentDB
def connect_to_mongodb():
    """
    connect to database mongodb
    output: database connection
    """
    try:
        host =os.environ.get('db_host')
        username = os.environ.get('db_username')
        password = os.environ.get('db_password')
        db_url = f"mongodb://{username}:{password}@{host}"
        client = MongoClient(db_url,tls=True, retryWrites=False)
        db = client[os.environ.get('db_name')]
        return db
    except Exception as e:
        print(f"Failed to connect to DocumentDB: {e}")
        return None