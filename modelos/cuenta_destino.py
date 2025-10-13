from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cuenta_destino(Base):
    __tablename__ = 'cuentas destino'
    id_cuenta_destino = Column(Integer,primary_key=True)
    tipo_cuenta_destino = Column(String(15), nullable=False)
    estado_cuenta_destino = Column(Boolean, nullable=False)