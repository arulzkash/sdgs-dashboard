from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb+srv://db:123@cluster0.vuwlz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.ardhicom

user_collection = database.get_collection("users")
address_collection = database.get_collection("addresses")
# Tambahkan koleksi lain sesuai kebutuhan
