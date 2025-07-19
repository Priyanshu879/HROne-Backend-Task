from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()
db = AsyncIOMotorClient(os.getenv("MONGO_URL")).get_database("HROne_Task")
