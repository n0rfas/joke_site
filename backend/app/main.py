from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from .schemas import JokeResponse
from .db import get_db
from .models import Joke

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/jokes/random/", response_model=JokeResponse)
def get_random_joke(db: Session = Depends(get_db)):
    joke = db.query(Joke).order_by(func.random()).first()
    if joke is None:
        raise HTTPException(status_code=404, detail="Joke not found")
    return joke
