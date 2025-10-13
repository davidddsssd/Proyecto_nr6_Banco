from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cuenta(Base):
    __tablename__ = 'cuentas'
    id_cuenta = Column(Integer,primary_key=True)
    numero_c = Column(String(15), nullable=False)
    saldo = Column(Float, nullable=False)
    fecha_apertura = Column(DateTime, nullable=True)
    tipo_cuenta = Column(String(15), nullable=False)
    estado_cuenta = Column(Boolean, nullable=False)
