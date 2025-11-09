from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from modelos.base import Base

class CuentaDestino(Base):
    __tablename__ = 'cuentas_destino'

    id_cuenta_destino = Column(Integer, primary_key=True, autoincrement=True)
    tipo_cuenta_destino = Column(String(15), nullable=False)
    estado_cuenta_destino = Column(Boolean, nullable=False)