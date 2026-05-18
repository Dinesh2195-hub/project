# Movie Recommender Demo

A simple full-stack movie recommendation system built with Python and FastAPI.

## Features

- FastAPI backend with movie list and recommendation API endpoints
- Static frontend with JavaScript fetching movie data
- Lightweight recommendation logic based on genre, ratings, and liked movies

## Run locally

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the app:

```bash
python -m uvicorn movie_recommender.main:app --reload
```

Open `http://127.0.0.1:8000/` in your browser.

## API

- `GET /api/movies` — list available movies
- `GET /api/recommend?genre=<genre>` — recommend movies in a genre
- `GET /api/recommend?liked_movie=<title>` — recommend movies similar to a liked movie
