"""
TODO:
1. UserCreate schema (for signup)
2. UserRead schema (for API response)
3. UserUpdate schema (future use)
4. Never expose password or hashed_password in responses
"""
from typing import Optional
from pydantic import BaseModel , EmailStr

class UserCreate(BaseModel):
    userName:str
    email: EmailStr
    password:str


class UserRead(BaseModel):
    pass  

class UserUpdate(BaseModel):
    pass



 
 
 