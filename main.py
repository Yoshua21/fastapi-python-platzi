from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

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
def get_movie(id:int):
    for item in movies:
        if item['id']==id:
            return item
    return []

@app.get('/movies/',tags=['movies'])
def get_movie_by_category(category:str,year:int):
    category=category.upper()
    for tipo in movies:
        if tipo['category']==category:
            return tipo
    return []

@app.post('/movies',tags=['movies'])
def create_movie(id: int= Body(), title:str=Body(), overview: str=Body(), year: int=Body(), rating: float=Body(), category: str=Body()):
    movies.append({
        "id":id,
        'title': title,
        'overview': overview,
        'year': year,
        'rating': rating,
        'category': category    
    })
    

@app.put('/movies/{id}',tags=['movies'])
def update_movie(id: int, title:str=Body(), overview: str=Body(), year: int=Body(), rating: float=Body(), category: str=Body()):
    for item in movies:
        if item['id']==id:
            item['title']= title
            item['overview']= overview
            item['year']= year
            item['rating']= rating
            item['category']= category    
            return movies
        return "Pelicula no encontrada" 
    
@app.delete('/movies/{id}',tags =['movies'])
def delte_movie(id: int):
    for item in movies:
        if item["id"]==id:
            movies.remove(item)
            return movies
        return "No localizado"