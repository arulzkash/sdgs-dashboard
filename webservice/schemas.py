from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional

class User(BaseModel):
    id: Optional[str] = Field(alias="_id")
    username: str
    email: str
    password: str
    is_admin: bool = False

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    is_admin: bool = False
