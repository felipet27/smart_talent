from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "Mi nombre es" : "Andres Felipe",
        "Próximo Ingeniero DevOps Junior de " : "Smart Talent",
        "Y esta es la solucion de la prueba": "Nos vemos pronto"
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
