"""
TODO:
1. Create User table
2. Fields:
   - id
   - email
   - hashed_password
   - role (user/admin)
   - is_active
   - created_at
3. Use SQLAlchemy ORM
4. Inherit from Base
"""
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from database import Base
from pydantic import EmailStr

class User(Base):
    __tablename__='user'
    id= Column(Integer, index=True, primary_key=True)
    email: EmailStr =Column(String,unique= True, index=True, nullable=False)
    hashed_password= Column(String, unique= True, nullable=False)
    role= Column(String)
    is_active= Column(Boolean)
    created_at = Column(DateTime)