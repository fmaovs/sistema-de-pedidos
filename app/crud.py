from sqlalchemy.orm import Session
from . import models, schemas

def get_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def delete_cliente(db: Session, cliente_id: int):
    db_cliente = get_cliente(db, cliente_id)
    db.delete(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

# Puedes crear funciones CRUD similares para Prenda y Pedido
def get_prenda(db: Session, prenda_id: int):
    return db.query(models.Prenda).filter(models.Prenda.id == prenda_id).first()

def create_prenda(db: Session, prenda: schemas.PrendaCreate):
    db_prenda = models.Prenda(**prenda.dict())
    db.add(db_prenda)
    db.commit()
    db.refresh(db_prenda)
    return db_prenda
    
def create_pedido(db: Session, pedido: schemas.PedidoCreate):
    return db.query(models.Pedido).filter(models.Pedido.id == pedido.id).first()


def delete_pedido(db: Session, pedido_id: int):
    db_pedido = get_cliente(db, pedido_id)
    db.delete(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

def get_pedido(db: Session, pedido_id: int):
    db_pedido = get_cliente(db, pedido_id)
    return db_pedido
