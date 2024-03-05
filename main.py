from fastapi import FastAPI
from database import get_all_movies, create_movie, test_connection
from fastapi.responses  import HTMLResponse
from pydantic import BaseModel
import bson

import database

app = FastAPI()
app.title = "App FastAPI"
app.version = "0.0.1"

class Movie(BaseModel):
    title : str
    year: int
    category: str

@app.get('/')
def welcome():
    return {"run": "API movie!"}

@app.get('/movies', tags=['movies'])
async def get_movies():
    # movies = await get_all_movies()
    # return movies
    await test_connection()
    return 

# @app.get('/movies/{id}', tags=['movies'])
# def get_movie_by_id(id: int):
#     for movie in movies:
#         if movie.id == id:
#             return movie
#     return []

# @app.get('/movies/', tags=['movies'])
# def get_movies_by_category(category: str, year: int):
#     return [movie for movie in movies if (movie["category"] == category and movie["year"] == year)]

@app.post('/movies', tags=['movies'])
async def save_move(movie: Movie):
    response = await create_movie(movie.model_dump())
    return response

# @app.put('/movies/', tags=['movies'])
# def update_movie(movie_input: Movie):
#     for movie in movies:
#         if movie["id"] == movie_input.id:
#             movie["title"] = movie_input.title
#             movie["year"] = movie_input.year
#             movie["category"] = movie_input.category
#             return True
#     return False
            
# @app.delete('/movies/{id}', tags=['movies'])
# def delete_movie(id: int):
#     print("Mooo1", movies)
#     print("ID", id)
#     for movie in movies:
#         if movie["id"] == id:
#             print("Mooo", movie)
#             movies.remove(movie)
#             return True
#     return False

