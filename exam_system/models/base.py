"""
Definición del modelo base para SQLAlchemy.

Este módulo define la clase base declarativa que será utilizada por todos los modelos
de SQLAlchemy en el proyecto. La clase `Base` es necesaria para que SQLAlchemy pueda
mapear las clases de Python a las tablas de la base de datos.
"""

# Importación de Módulos
from sqlalchemy.orm import declarative_base

# Variables Globales
# Base es la clase base a partir de la cual se definirán todos los modelos del sistema.
Base = declarative_base()
