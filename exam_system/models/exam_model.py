"""
Modelo de datos para exámenes.

Este módulo define el modelo `ExamModel`, que representa una tabla de exámenes en la base de datos.
Cada examen tiene un título y una relación con múltiples preguntas (representadas por `QuestionModel`).
"""

# Importación de Módulos
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


# Declaración de Clases
class ExamModel(Base):
    """
    Modelo ORM que representa la tabla 'exams'.
    """
    __tablename__ = 'exams'

    # ID del examen (clave primaria)
    id = Column(Integer, primary_key=True)
    # Título del examen (campo obligatorio)
    title = Column(String, nullable=False)
    # Relación uno-a-muchos con la tabla 'questions'
    # Un examen puede tener múltiples preguntas asociadas
    questions = relationship("QuestionModel", back_populates="exam")