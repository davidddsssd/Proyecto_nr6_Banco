#pip install sqlalchemy
#pip install mysql-connector-python
#pip install prettytable

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from auxiliares import usuario_db, servidor_db, puerto_db, nombre_db

# pip install sqlalchemy
# pip install mysql-connector-python

# Definir cadena de conexion
# mysql+mysqlconnector://user:password@host:port/database_name
# Reemplazar user, password, host, port, y database con sus credenciales de DB
url_db = f"mysql+mysqlconnector://{usuario_db}:@{servidor_db}:{puerto_db}/{nombre_db}"
motor_db = create_engine(url_db)
Session = sessionmaker(bind=motor_db)
sesion = Session()