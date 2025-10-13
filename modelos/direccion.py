from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Direccion(Base):
    __tablename__ = 'direcciones'
    id_direccion = Column(Integer,primary_key=True)
    comuna = Column(String(30), nullable=False)
    calle = Column(String(20), nullable=False)
    departamento = Column(String(20), nullable=True)
    numero_d = Column(String(15), nullable=False)