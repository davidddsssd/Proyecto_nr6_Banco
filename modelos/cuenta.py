from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from modelos.base import Base

class Cuenta(Base):
    __tablename__ = 'cuentas'

    id_cuenta = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente'))
    numero_c = Column(String(20), nullable=False, unique=True)
    saldo = Column(Integer, nullable=False)
    fecha_apertura = Column(DateTime, nullable=False)
    tipo_cuenta = Column(Enum('corriente', 'ahorro', 'vista'), nullable=False)
    estado_cuenta = Column(Boolean, nullable=False)