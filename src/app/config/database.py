import motor.motor_asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME", "ecommerce")

class MongoDB:
    def __init__(self):
        """Initialize MongoDB connection"""
        self.client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI, maxPoolSize=10, minPoolSize=1)
        self.db = self.client[DATABASE_NAME]

    def get_database(self):
        """Retrieve the database instance"""
        return self.db

# Singleton instance
mongodb = MongoDB()

# Utility function for accessing the database
def get_database():
    """Function to return MongoDB instance"""
    return mongodb.get_database()
