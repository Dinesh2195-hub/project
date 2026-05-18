from pydantic import BaseModel


class Movie(BaseModel):
    title: str
    genre: str
    rating: float
    votes: int
    year: int
    description: str
