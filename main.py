from fastapi import FastAPI
from fastapi.responses import HTMLResponse

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
      {
        'id': 2,
        'title': "moana",
        'overview': "PElicula de disney ...",
        'year': '20222',
        'rating': 9,
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