from pydantic import BaseModel,field_validator
from typing import Optional


class User(BaseModel):
    
    user_name: str
    email: str
    password: str
    phone_number : Optional[str] = None
    
    
    class Config:
        orm_mode = True

    @field_validator('password')
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return value

    
    
            
