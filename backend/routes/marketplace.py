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

router = APIRouter(prefix="/marketplace")


@router.post("/create",
             dependencies=[Depends(Limit(times=20, seconds=5))],
             status_code=201
             )
async def create(
        marketplace: CreateMarketplace, 
        request: Request, db: Session = Depends(get_db)
        ) -> JSONResponse:

    pass