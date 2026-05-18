from typing import Dict, List, Optional

MOVIES = [
    {
        "title": "The Last Horizon",
        "genre": "Sci-Fi",
        "rating": 8.7,
        "votes": 12453,
        "year": 2024,
        "description": "A team of explorers searches for a new home beyond the stars.",
    },
    {
        "title": "Silent Echo",
        "genre": "Drama",
        "rating": 8.1,
        "votes": 8790,
        "year": 2023,
        "description": "A quiet musician learns to speak through the power of community.",
    },
    {
        "title": "Midnight Chase",
        "genre": "Action",
        "rating": 7.9,
        "votes": 10234,
        "year": 2022,
        "description": "A fast-paced thriller where every second counts and every choice matters.",
    },
    {
        "title": "Whispering Pines",
        "genre": "Horror",
        "rating": 7.4,
        "votes": 6512,
        "year": 2021,
        "description": "Strange events unfold when a family moves into an ancient woodland estate.",
    },
    {
        "title": "Golden Harvest",
        "genre": "Drama",
        "rating": 8.3,
        "votes": 9184,
        "year": 2020,
        "description": "A story of friendship and resilience on a small countryside farm.",
    },
    {
        "title": "Neon Drift",
        "genre": "Sci-Fi",
        "rating": 8.0,
        "votes": 10820,
        "year": 2024,
        "description": "Street racers and rogue AIs collide in a neon-lit future city.",
    },
    {
        "title": "Rising Ember",
        "genre": "Action",
        "rating": 7.8,
        "votes": 7711,
        "year": 2023,
        "description": "A former agent returns for one last mission to protect the ones she loves.",
    },
]


def recommend_movies(
    genre: Optional[str] = None,
    liked_movie: Optional[str] = None,
    limit: int = 5,
) -> List[Dict]:
    """Return a small list of recommended movies."""
    if liked_movie:
        liked = next(
            (movie for movie in MOVIES if movie["title"].lower() == liked_movie.lower()),
            None,
        )
        if liked:
            return [
                movie
                for movie in MOVIES
                if movie["genre"] == liked["genre"] and movie["title"] != liked["title"]
            ][:limit]

    if genre:
        return [movie for movie in MOVIES if movie["genre"].lower() == genre.lower()][:limit]

    return sorted(MOVIES, key=lambda movie: (-movie["rating"], -movie["votes"]))[:limit]
