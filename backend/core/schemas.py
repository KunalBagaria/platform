import uuid
from datetime import datetime
from sqlalchemy import (
                        Column, 
                        String, 
                        Integer, 
                        DateTime, 
                        Text,
                        ForeignKey,
                        Boolean
                        )
from sqlalchemy.orm import relationship
from core.db import Base
from utils import get_random_avatar, get_random_banner

def get_uuid():
    return uuid.uuid4().hex

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    public_key = Column(String(length=44), nullable=False, unique=True)
    name = Column(String(length=25), nullable=True)
    seller = Column(Boolean, default=False, nullable=False)
    joined_on = Column(DateTime, default=datetime.utcnow, nullable=False)

    hash = relationship("Hash", backref="users", uselist=False)
    seller_user = relationship("Seller", backref="users", uselist=False)


class Seller(Base):
    __tablename__ = "sellers"

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True, index=True)
    avatar = Column(String(100), default=get_random_avatar, nullable=False)
    banner = Column(String(100), default=get_random_banner, nullable=False)
    verified = Column(Boolean, default=False, nullable=False)
    rating  = Column(Integer, default=0, nullable=False)
    total_revenue  = Column(Integer, default=0, nullable=False)

    marketplaces = relationship("Marketplace", back_populates="seller", passive_deletes=True)


class Marketplace(Base):
    __tablename__ = "marketplaces"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(length=25), nullable=False)
    description = Column(Text, nullable=True)
    logo = Column(String(100), default=get_random_avatar, nullable=False)
    banner = Column(String(100), default=get_random_banner, nullable=False)
    email = Column(String(length=25), nullable=True)
    created_on = Column(DateTime, default=datetime.utcnow, nullable=False)

    seller_id = Column(Integer, ForeignKey('sellers.user_id', ondelete='CASCADE'))
    seller = relationship("Seller", back_populates="marketplaces")


class Hash(Base):
    __tablename__ = "hashes"

    user_public_key = Column(Integer, ForeignKey('users.public_key'), primary_key=True, index=True)
    hash = Column(String(length=32), default=get_uuid, nullable=False)
