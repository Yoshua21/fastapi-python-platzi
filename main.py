from fastapi import FastAPI

app=FastAPI() #se crea una instancia de fastAPI

@app.get('/')
def messaege():
    return "Duncan se la come"
