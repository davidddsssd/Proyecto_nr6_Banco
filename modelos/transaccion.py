from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Transaccion(Base):
    __tablename__ = 'Transacciones'
    id_transaccion = Column(Integer,primary_key=True)
    tipo_transaccion = Column(String(12), nullable=False)
    fecha_transaccion = Column(DateTime, nullable=False)
    monto = Column(float, nullable=False)