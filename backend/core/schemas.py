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


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    public_key = Column(String(length=44), nullable=False, unique=True)
    name = Column(String(length=25), nullable=True)
    seller = Column(Boolean, default=False, nullable=False)
    joined_on = Column(DateTime, default=datetime.utcnow, nullable=False)

    seller_user = relationship("Seller", backref="users", uselist=False)


class Seller(Base):
    __tablename__ = "sellers"

    avatar = Column(String(100), default=get_random_avatar, nullable=False)
    banner = Column(String(100), default=get_random_banner, nullable=False)
    verified = Column(Boolean, default=False, nullable=False)
    seller = Column(Boolean, default=False, nullable=False)
    rating  = Column(Integer, default=0, nullable=False)
    total_revenue  = Column(Integer, default=0, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True, autoincrement=True, index=True)
#     marketplace = relationship("Marketplace", back_populates="sellers")


# class Marketplace(Base):
#     __tablename__ = "marketplaces"

#     id = Column(Integer, primary_key=True, autoincrement=True, index=True)
#     name = Column(String(length=25), nullable=False)
#     description = Column(Text, nullable=True)
#     logo = Column(String(100), default=get_random_avatar, nullable=False)
#     banner = Column(String(100), default=get_random_banner, nullable=False)
#     email = Column(String(length=25), nullable=True)
#     created_on = Column(DateTime, default=datetime.utcnow, nullable=False)

#     seller_id = Column(Integer, ForeignKey('users.id'))
#     seller = relationship("Seller", back_populates="marketplaces")


class Signature(Base):
    __tablename__ = "signatures"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    public_key = Column(String(length=44), nullable=False)
    hash = Column(String(length=44), nullable=False)
