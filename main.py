from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel,Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2022)
    rating: float = Field(ge=0.0, le=10.0)
    category: str = Field(min_length=5, max_length=15)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Shrek",
                "overview": "Ogro timido encuentra amor inesperado.",
                "year": 2001,
                "rating": 7.8,
                "category": "Comedia"
            }
        }

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'ACCION'    
    },
      {
        'id':2,
        'title': "moana",
        'overview': "PElicula de disney ...",
        'year': '20222',
        'rating': 9,
        'category': 'Animada'    
    } ,
      {
        'id':3,
        'title': "shuek",
        'overview': "PElicula de disney ...",
        'year': '2017',
        'rating': 7,
        'category': 'Animada'    
    } 
]

app=FastAPI() #se crea una instancia de fastAPI
app.title ="Aplicacion con FasAPI " #Se coloca nobre a la documentacion
app.version="0.0.1" #Se coloca la version que se esta viendo

@app.get('/',tags=['home'])#se crea la ruta y se le conoca una etiqueta
def messaege():
    return HTMLResponse('<h1>Duncan de la come</h1>')

@app.get('/movies',tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}',tags=['movies']) #Se creo un api donde se espera a que se envie un parametro en la ruta para poder repsonder de acuerdo al parametro
def get_movie(id:int=Path(ge=1,le=2000)):
    for item in movies:
        if item['id']==id:
            return item
    return []

@app.get('/movies/',tags=['movies'])
def get_movie_by_category(category:str=Query(min_length=5,max_length=15)):
    for tipo in movies:
        if tipo['category']==category:
            return tipo
    return []

@app.post('/movies',tags=['movies'])
def create_movie(Movis: Movie):
    movies.append(Movis)
    return movies
    

@app.put('/movies/{id}',tags=['movies'])
def update_movie(id: int,movie:Movie):
    for item in movies:
        if item['id'] == id:
            item['title']= Movie.title
            item['overview']= Movie.overview
            item['year']= Movie.year
            item['rating']= Movie.rating
            item['category']= Movie.category    
            return movies
        return "Pelicula no encontrada" 
    
@app.delete('/movies/{id}',tags =['movies'])
def delte_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies
        return "No localizado"