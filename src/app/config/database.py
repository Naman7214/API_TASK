import motor.motor_asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME", "ecommerce")

class MongoDB:
    def __init__(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI, maxPoolSize=10, minPoolSize=1)
        self.db = self.client[DATABASE_NAME]

    async def get_database(self):
        return self.db

# Singleton instance
mongodb = MongoDB()
