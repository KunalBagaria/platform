from pydantic import BaseModel
from typing import Optional

class CreateMarketplace(BaseModel):
    seller_public_key: str
    name: str
    description: str
    logo: Optional[str]
    banner: Optional[str]
    email: Optional[str]
    public_key: str
    signature: dict

class UpdateMarketPlace(BaseModel):
    name: Optional[str]
    description: Optional[str]
    logo: Optional[str]
    banner: Optional[str]
    email: Optional[str]
    public_key: str
    signature: dict

class CreateUser(BaseModel):
    pass