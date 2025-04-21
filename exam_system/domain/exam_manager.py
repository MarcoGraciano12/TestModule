"""
Módulo para la gestión de exámenes mediante SQLAlchemy.

Contiene la clase ExamManager que permite crear, actualizar, eliminar y listar
exámenes persistidos en una base de datos relacional.
"""

# Importación de Módulos
from exam_system.models.exam_model import ExamModel
from exam_system.models.question_model import QuestionModel
from sqlalchemy.orm import Session
from .exam import Exam
from .question import Question
from sqlalchemy.exc import SQLAlchemyError


# Declaración de Clases
class ExamManager:
    """
     Gestor de exámenes que interactúa con la base de datos.

    Métodos:
        - create_exam(exam): Crea un nuevo examen en la base de datos.
        - list_exams(): Retorna todos los exámenes almacenados.
        - delete_exam(exam_id): Elimina un examen por ID.
        - update_exam(exam_id, updated_exam): Actualiza el título y preguntas del examen.
    """

    def __init__(self, session: Session):
        """
         Inicializa el gestor con una sesión activa de SQLAlchemy.

        Args:
            session (Session): Sesión de base de datos SQLAlchemy.
        """
        self.session = session

    def create_exam(self, exam: Exam):
        """
        Crea un nuevo examen en la base de datos junto con sus preguntas.

        Args:
            exam (Exam): Instancia de la clase Exam con título y preguntas.

        Raises:
            RuntimeError: Si ocurre un error al guardar el examen en la base de datos.
        """
        try:
            exam_model = ExamModel(title=exam.title)
            for question in exam.questions:
                q_model = QuestionModel(prompt=question.prompt, answer=question.answer)
                exam_model.questions.append(q_model)

            self.session.add(exam_model)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise RuntimeError(f"Error while creating exam: {e}")

    def list_exams(self):
        """
        Recupera todos los exámenes registrados en la base de datos.

        Returns:
            List[ExamModel]: Lista de instancias de ExamModel.

        Raises:
            RuntimeError: Sí ocurre un error al consultar los exámenes.
        """
        try:
            return self.session.query(ExamModel).all()
        except SQLAlchemyError as e:
            raise RuntimeError(f"Error fetching exams: {e}")

    def delete_exam(self, exam_id: int):
        """
        Elimina un examen existente por su ID.

        Args:
            exam_id (int): Identificador del examen a eliminar.

        Raises:
            ValueError: Si no existe un examen con el ID proporcionado.
            RuntimeError: Sí ocurre un error durante la eliminación.
        """
        try:
            exam = self.session.get(ExamModel, exam_id)
            if not exam:
                raise ValueError(f"Exam with ID {exam_id} not found.")
            self.session.delete(exam)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise RuntimeError(f"Error deleting exam: {e}")
