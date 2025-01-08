from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import crud
from schemas import User, UserCreate

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/users/", response_model=list[User])
async def get_all_users_endpoint():
    users = await crud.get_all_users()
    return users


@app.post("/users/", response_model=User)
async def create_user_endpoint(user: UserCreate):
    new_user = await crud.create_user(user)
    return new_user


@app.get("/users/{id}", response_model=User)
async def get_user_endpoint(id: str):
    user = await crud.get_user(id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.put("/users/{id}", response_model=User)
async def update_user_endpoint(id: str, user: UserCreate):
    updated_user = await crud.update_user(id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@app.delete("/users/{id}")
async def delete_user_endpoint(id: str):
    await crud.delete_user(id)
    return {"message": "User deleted successfully"}
