from pydantic import BaseModel


class JokeResponse(BaseModel):
    text: str
