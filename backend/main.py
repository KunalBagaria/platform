import os
from fastapi import FastAPI
from aioredis import from_url
from dotenv import load_dotenv
from core.db import engine, Base
from fastapi.param_functions import Depends
from core.ratelimit import RateLimiter, Limit
from fastapi.middleware.cors import CORSMiddleware
from routes import marketplace


load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(marketplace.router)


@app.on_event("startup")
async def startup() -> None:
    if not os.environ.get("REDIS_URL"):
        inp = input("\nRedis URL not found, do you wish to run without rate limit? [y/n]\n")
        if inp != "y":
            raise KeyError("You must setup REDIS_URL environment variable.")

    if inp != "y":
        redis = await from_url(os.environ["REDIS_URL"], encoding="utf8")
        await RateLimiter.init(redis)
    else:
        await RateLimiter.init(no_effect=True)
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown() -> None:
    await RateLimiter.close()

@app.get("/", dependencies=[Depends(Limit(times=20, seconds=1))])
async def root() -> dict:
    return {"message": "hi"}