from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter()

@router.post("/pedido/", response_model=schemas.Pedido)
def create_cliente(cliente: schemas.PedidoCreate, db: Session = Depends(get_db)):
    return crud.create_pedido(db=db, pedido = pedido)

@router.get("/pedido/{pedido_id}", response_model=schemas.Pedido)
def read_pedido(pedido_id: int, db: Session = Depends(get_db)):
    db_pedido = crud.get_pedido(db, pedido_id = pedido_id)
    if db_pedido is None:
        raise HTTPException(status_code = 404, detail= "Pedido not found")
    return db_pedido
