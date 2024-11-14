# app/models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), index=True)
    telefono = Column(Integer, unique=True, index=True)

    pedidos = relationship("Pedido", back_populates="cliente")

class Prenda(Base):
    __tablename__ = "prendas"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), index=True)
    precio = Column(Float)

    pedidos = relationship("Pedido", back_populates="prenda")

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    prenda_id = Column(Integer, ForeignKey("prendas.id"))
    cantidad = Column(Integer)

    cliente = relationship("Cliente", back_populates="pedidos")
    prenda = relationship("Prenda", back_populates="pedidos")
