from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from auxiliares import usuario_db, servidor_db, puerto_db, nombre_db
from modelos.base import Base

url_db = f"mysql+mysqlconnector://{usuario_db}:@{servidor_db}:{puerto_db}/{nombre_db}"

motor_db = create_engine(url_db, echo=False)
Base.metadata.create_all(motor_db)
Session = sessionmaker(bind=motor_db)