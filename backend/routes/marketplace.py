from core.db import get_db
from sqlalchemy.orm import Session
from core.ratelimit import Limit
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends
from core.models import (
                CreateMarketplace,
                UpdateMarketPlace
                )
from core.schemas import (
        User,
        Seller,
        Marketplace,
        Hash
    )
from utils import verify_signature


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
    db.flush() # Flushing to get the user id
    seller = Seller(user_id=user.id)
    db.add(seller)
    user_hash = Hash(user_public_key=user.public_key)
    db.add(user_hash)
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


@router.put("/update/{id}",
             dependencies=[Depends(Limit(times=20, seconds=5))],
             status_code=200
             )
async def update(
        marketplace: UpdateMarketPlace, 
        id: int,
        db: Session = Depends(get_db)
        ) -> JSONResponse:
    
    signature = marketplace.signature
    signature = signature["data"]
    user_hash = db.query(Hash).filter_by(user_public_key=marketplace.public_key)
    verify = verify_signature(user_hash, signature, marketplace.public_key)

    if not verify:
        return JSONResponse(
            status_code=403,
            content={"error": "Error verifying signature"}
        )

    marketplace = db.query(Marketplace).filter_by(id=id).first()
    if marketplace:
        data_dict = marketplace.dict(exclude_unset=True)
        
        for key, value in data_dict.items():
            setattr(marketplace, key, value)
        db.commit(marketplace)
        db.refresh(marketplace)
        return marketplace
        
    return JSONResponse(
        status_code=400,
        content={"error": "Marketplace does not exist"}
    )

