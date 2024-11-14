from fastapi import FastAPI
from .database import engine, Base
from .routers import cliente, prenda, pedido

app = FastAPI()

# Crear tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)

app.include_router(cliente.router)
#app.include_router(prenda.router)
#app.include_router(pedido.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de pedidos"}
