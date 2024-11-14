from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter()

@router.post("/prendas/", response_model=schemas.Prenda)
def create_prenda(prenda: schemas.PrendaCreate, db: Session = Depends(get_db)):
    return crud.create_prenda(db=db, prenda=prenda)

@router.get("/prendas/{prenda_id}", response_model=schemas.Prenda)
def read_prenda(prenda_id: int, db: Session = Depends(get_db)):
    db_prenda = crud.get_prenda(db, prenda_id=prenda_id)
    if db_prenda is None:
        raise HTTPException(status_code=404, detail="Prenda not found")
    return db_prenda
