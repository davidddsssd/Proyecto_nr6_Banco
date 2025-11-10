from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from modelos.base import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    id_direccion = Column(Integer, ForeignKey('direcciones.id_direccion'))
    nombre = Column(String(30), nullable=False)
    apellido = Column(String(30), nullable=False)
    rut = Column(String(12), nullable=False, unique=True)
    telefono = Column(String(15), nullable=False, unique=True)
    mail = Column(String(50), nullable=True)
    estado_cliente = Column(Boolean, nullable=False, default=True)