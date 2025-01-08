from bson import ObjectId
from schemas import User, UserCreate
from database import user_collection


async def get_all_users() -> list[User]:
    users = []
    async for user in user_collection.find():
        user["_id"] = str(user["_id"])
        users.append(User(**user))
    return users


async def get_user(id: str) -> User:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        user["_id"] = str(user["_id"])
        return User(**user)
    return None


async def create_user(user: UserCreate) -> User:
    user_dict = user.dict()
    result = await user_collection.insert_one(user_dict)
    user_dict["_id"] = str(result.inserted_id)
    return User(**user_dict)


async def update_user(id: str, user: UserCreate) -> User:
    user_dict = user.dict()
    result = await user_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": user_dict}
    )
    if result.modified_count:
        user_dict["_id"] = id
        return User(**user_dict)
    return None


async def delete_user(id: str):
    await user_collection.delete_one({"_id": ObjectId(id)})
