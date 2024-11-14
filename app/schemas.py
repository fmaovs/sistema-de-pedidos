# app/schemas.py
from pydantic import BaseModel
from typing import List, Optional

class ClienteBase(BaseModel):
    nombre: str
    telefono: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int
    class Config:
        orm_mode = True

class PrendaBase(BaseModel):
    nombre: str
    precio: float

class PrendaCreate(PrendaBase):
    pass

class Prenda(PrendaBase):
    id: int
    class Config:
        orm_mode = True

class PedidoBase(BaseModel):
    cliente_id: int
    prenda_id: int
    cantidad: int

class PedidoCreate(PedidoBase):
    pass

class Pedido(PedidoBase):
    id: int
    class Config:
        orm_mode = True
