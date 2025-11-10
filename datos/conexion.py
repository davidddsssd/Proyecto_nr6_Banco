from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from auxiliares import usuario_db, servidor_db, puerto_db, nombre_db
from modelos.base import Base

#Cadena de conexión
url_db = f"mysql+mysqlconnector://{usuario_db}:@{servidor_db}:{puerto_db}/{nombre_db}"

#Crear el motor de conexión
motor_db = create_engine(url_db)

#Crear las tablas si no existen (esto no borra nada)
Base.metadata.create_all(motor_db)

# Crear la clase Session
Session = sessionmaker(bind=motor_db)