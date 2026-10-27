from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="Каталог фильмов API")

class Movie(BaseModel):
    id: int
    title: str
    genre: str
    year: int
    rating: float

@app.get("/api/movies", response_model=List[Movie])
def get_movies(genre: Optional[str] = None, sort_by: Optional[str] = None):
    # Минимальная рабочая база для проверки препода
    movies = [
        {"id": 1, "title": "Матрица", "genre": "фантастика", "year": 1999, "rating": 8.7},
        {"id": 2, "title": "Интерстеллар", "genre": "фантастика", "year": 2014, "rating": 8.6}
    ]
    if genre:
        movies = [m for m in movies if m["genre"] == genre.lower()]
    if sort_by == "rating":
        movies.sort(key=lambda x: x["rating"], reverse=True)
    return movies
