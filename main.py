import uuid
import json
import os

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
USER_FILE = "users.json"


def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    try:
        with open(USER_FILE, "r") as f:
            content = f.read().strip()
            return json.loads(content) if content else {}
    except json.JSONDecodeError:
        # Handle the case where the file is empty or corrupted
        print(f"Error reading {USER_FILE}. Returning empty user list.")
        return {}


def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=2)


class User(BaseModel):
    name: str
    email: str


@app.get("/")
async def root():
    return {"message": "Welcome to the User Management API!"}


@app.get("/users")
async def get_users():
    return list(load_users().values())


@app.post("/users")
def create_user(user: User):
    users = load_users()
    user_id = str(uuid.uuid4())
    users[user_id] = {"id": user_id, "user": user.dict()}
    save_users(users)
    return users[user_id]
