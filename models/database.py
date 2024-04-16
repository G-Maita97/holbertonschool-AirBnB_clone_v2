from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configurar el motor de SQLAlchemy para MySQL
engine = create_engine('mysql+mysqlconnector://gustavo:@localhost/db')

# Crear una clase de sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)

# Crear una sesión para interactuar con la base de datos
db_session = Session()
