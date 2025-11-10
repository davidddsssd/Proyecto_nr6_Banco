from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from modelos.base import Base

class Transaccion(Base):
    __tablename__ = 'transacciones'

    id_transaccion = Column(Integer, primary_key=True, autoincrement=True)
    id_cuenta = Column(Integer, ForeignKey('cuentas.id_cuenta'), nullable=False)
    id_cuenta_destino = Column(Integer, ForeignKey('cuentas_destino.id_cuenta_destino'), nullable=True)
    tipo_transaccion = Column(String(12), nullable=False)
    fecha_transaccion = Column(DateTime, nullable=False)
    monto = Column(Integer, nullable=False)
    descripcion = Column(String(100))