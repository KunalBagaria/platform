from core.db import get_db
from sqlalchemy.orm import Session
from core.ratelimit import Limit
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, Request
from core.models import (
                CreateUser, 
                CreateSeller,
                CreateMarketplace
                )
from core.schemas import (
        User,
        Seller,
        Marketplace
    )

router = APIRouter(prefix="/marketplace")


@router.post("/create",
             dependencies=[Depends(Limit(times=20, seconds=5))],
             status_code=201
             )
async def create(
        marketplace: CreateMarketplace, 
        db: Session = Depends(get_db)
        ) -> JSONResponse:
    
    user = User(public_key=marketplace.seller_public_key, seller=True)
    db.add(user)
    seller = Seller(user_id=user.id)
    db.add(seller)
    db.commit()
    marketplace = Marketplace(
                            name=marketplace.name,
                            description=marketplace.description,
                            logo=marketplace.logo,
                            banner=marketplace.banner,
                            email=marketplace.email,
                            seller_id=seller.user_id,
                            )
    db.add(marketplace)
    db.commit()
    db.refresh(marketplace)
    return marketplace
