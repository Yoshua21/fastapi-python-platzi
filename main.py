from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app=FastAPI() #se crea una instancia de fastAPI
app.title ="Aplicacion con FasAPI " #Se coloca nobre a la documentacion
app.version="0.0.1" #Se coloca la version que se esta viendo

@app.get('/',tags=['home'])#se crea la ruta y se le conoca una etiqueta
def messaege():
    return HTMLResponse('<h1>"Duncan de la come"</h1>')
