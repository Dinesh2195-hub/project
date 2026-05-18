from fastapi.testclient import TestClient

from movie_recommender.main import app

client = TestClient(app)


def test_list_movies() -> None:
    response = client.get("/api/movies")
    assert response.status_code == 200
    movies = response.json()
    assert any(movie["title"] == "The Last Horizon" for movie in movies)


def test_recommend_by_genre() -> None:
    response = client.get("/api/recommend", params={"genre": "Drama"})
    assert response.status_code == 200
    recommendations = response.json()
    assert len(recommendations) > 0
    assert all(movie["genre"] == "Drama" for movie in recommendations)


def test_recommend_by_liked_movie() -> None:
    response = client.get("/api/recommend", params={"liked_movie": "Silent Echo"})
    assert response.status_code == 200
    recommendations = response.json()
    assert len(recommendations) > 0
    assert all(movie["title"] != "Silent Echo" for movie in recommendations)
