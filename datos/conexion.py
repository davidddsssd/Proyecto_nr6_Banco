#pip install sqlalchemy
#pip install mysql-connector-python
#pip install prettytable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#User, password, host, port, database con sus credenciales DB
DATABASE_URL = "mysql+sqlconnector://root:@localhost:3306/proyecto_banco"
motor_db = create_engine(DATABASE_URL, pool_pre_ping=True)
Session = sessionmaker(bind=motor_db)