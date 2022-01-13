from pydantic import BaseModel
from typing import Optional

class CreateUser(BaseModel):
    public_key: str
    name: str
    seller: bool
    seller_user_id: int

class CreateSeller(BaseModel):
    bio: str
    avatar: Optional[str]
    banner: Optional[str]

class CreateMarketplace(BaseModel):
    seller_public_key: str
    name: str
    description: str
    logo: Optional[str]
    banner: Optional[str]
    email: Optional[str]
