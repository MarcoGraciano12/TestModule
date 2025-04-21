"""
Módulo de inicialización de la base de datos.

Este módulo configura el motor de SQLAlchemy para conectarse a la base de datos y proporciona
una función para inicializar la base de datos, creando todas las tablas definidas en los modelos.

Se utiliza la URL de la base de datos especificada en la variable de entorno `DATABASE_URL`,
o bien una URL por defecto si la variable de entorno no está configurada.
"""

# Importación de Módulos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from exam_system.models.base import Base
import os

# Variables Globales
# URL de la base de datos, se obtiene del entorno o usa una por defecto
url = r'C:\Users\magraciano\PycharmProjects\TestModule\exam_system\db\exam.db'
DB_URL = os.getenv("DATABASE_URL", f"sqlite:///{url}")
# Crear el motor de base de datos con la URL configurada
engine = create_engine(DB_URL, echo=False)
# Crear una fábrica de sesiones locales para interactuar con la base de datos
SessionLocal = sessionmaker(bind=engine)

# Declaración de Funciones
def init_db():
    """
    Inicializa la base de datos creando todas las tablas definidas en los modelos.

    Este método utiliza `Base.metadata.create_all()` para asegurarse de que las tablas
    de la base de datos se creen si no existen aún. No modifica las tablas existentes.
    """
    Base.metadata.create_all(bind=engine)
