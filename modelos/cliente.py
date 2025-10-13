from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'Clientes'
    id_cliente = Column(Integer,primary_key=True)
    nombre = Column(String(30), nullable=False)
    apellido = Column(String(30), nullable=False)
    rut = Column(String(12), nullable=False)
    telefono = Column(Integer, nullable=False)
    mail = Column(String(20), nullable=True)