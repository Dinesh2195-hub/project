from pathlib import Path
from typing import List, Optional

from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .data import MOVIES, recommend_movies
from .schemas import Movie

app = FastAPI(
    title="Movie Recommender",
    description="A simple movie recommendation backend with a static frontend.",
    version="0.1.0",
)

static_dir = Path(__file__).resolve().parent / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/", response_class=FileResponse)
def homepage() -> Path:
    return static_dir / "index.html"


@app.get("/api/movies", response_model=List[Movie])
def list_movies(
    genre: Optional[str] = Query(None, description="Filter movies by genre"),
    min_rating: float = Query(0.0, ge=0.0, le=10.0, description="Minimum rating filter"),
) -> List[Movie]:
    filtered = [movie for movie in MOVIES if movie["rating"] >= min_rating]
    if genre:
        filtered = [movie for movie in filtered if movie["genre"].lower() == genre.lower()]
    return [Movie(**movie) for movie in filtered]


@app.get("/api/recommend", response_model=List[Movie])
def recommend(
    genre: Optional[str] = Query(None, description="Recommend movies from a genre"),
    liked_movie: Optional[str] = Query(None, description="Recommend movies based on a liked title"),
    limit: int = Query(5, ge=1, le=10, description="Number of recommendations to return"),
) -> List[Movie]:
    recommendations = recommend_movies(genre=genre, liked_movie=liked_movie, limit=limit)
    return [Movie(**movie) for movie in recommendations]
