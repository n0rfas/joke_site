from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func, select

from app.dependencies import AsyncSessionDep
from app.models import Joke
from app.schemas import JokeResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/api/jokes/random/", response_model=JokeResponse)
async def get_random_joke(db: AsyncSessionDep):
    result = await db.execute(select(Joke).order_by(func.random()).limit(1))
    joke = result.scalar_one_or_none()
    if joke is None:
        raise HTTPException(status_code=404, detail="Joke not found")
    return joke


@app.get("/api/jokes/{id}/", response_model=JokeResponse)
async def get_joke_by_id(id: int, db: AsyncSessionDep):
    result = await db.execute(select(Joke).filter(Joke.id == id))
    joke = result.scalar_one_or_none()
    if joke is None:
        raise HTTPException(status_code=404, detail="Joke not found")
    return joke


@app.get("/api/jokes/", response_model=list[JokeResponse])
async def get_all_jokes(db: AsyncSessionDep):
    result = await db.execute(select(Joke))
    jokes = result.scalars().all()
    return jokes
