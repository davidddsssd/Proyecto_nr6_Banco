from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from auxiliares import usuario_db, servidor_db, puerto_db, nombre_db
from modelos.base import Base

# Nota: evitar efectos secundarios (create_all / conexión) en tiempo de importación.
# Creamos el engine y las tablas de forma perezosa cuando realmente se necesiten.

_engine = None

def get_engine():
	"""Devuelve el engine de SQLAlchemy, creándolo la primera vez que se solicita."""
	global _engine
	if _engine is None:
		# Cadena de conexión (sin contraseña explícita aquí)
		url_db = f"mysql+mysqlconnector://{usuario_db}:@{servidor_db}:{puerto_db}/{nombre_db}"
		_engine = create_engine(url_db, echo=False)
	return _engine

def inicializar_bd():
	"""Crea las tablas en la base de datos si no existen. Llamar explícitamente desde el punto de arranque si se desea."""
	engine = get_engine()
	Base.metadata.create_all(engine)

def _session_factory():
	"""Fábrica interna que devuelve una sesión vinculada al engine (crea engine si hace falta)."""
	engine = get_engine()
	SessionLocal = sessionmaker(bind=engine)
	return SessionLocal()

# Exponer `Session` como callable para mantener la API existente: `session = Session()`
Session = _session_factory