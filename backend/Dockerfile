FROM python:3

COPY / /api

WORKDIR /api

RUN pip install aioredis fastapi psycopg2 solathon python-dotenv sqlalchemy uvicorn

CMD uvicorn main:app --host 0.0.0.0 --port ${PORT}