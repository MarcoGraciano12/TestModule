"""
Modelo de datos para preguntas de exámenes.

Este módulo define el modelo `QuestionModel`, que representa la tabla de preguntas
asociadas a los exámenes. Cada pregunta pertenece a un examen específico y contiene
un enunciado (prompt) y una respuesta.
"""

# Importación de Módulos
from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base
from sqlalchemy.orm import relationship


class QuestionModel(Base):
    """
     Modelo ORM que representa la tabla 'questions'.
    """
    __tablename__ = 'questions'

    # ID de la pregunta (clave primaria)
    id = Column(Integer, primary_key=True)
    # Enunciado de la pregunta (campo obligatorio)
    prompt = Column(String, nullable=False)
    # Respuesta a la pregunta (campo obligatorio)
    answer = Column(String, nullable=False)
    # Clave foránea que vincula la pregunta con un examen
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False)
    # Relación muchos-a-uno con el modelo ExamModel
    exam = relationship("ExamModel", back_populates="questions")
