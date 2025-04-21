"""
Clase que representa un examen compuesto por una lista de preguntas.

Esta clase proporciona métodos para agregar, eliminar y actualizar preguntas
dentro de un examen en memoria. Está pensada para ser utilizada de forma lógica
en el manejo de exámenes, independiente del modelo de base de datos.
"""

# Declaración de Clases
class Exam:
    """
    Representa un examen con un título y una colección de preguntas.
    """
    def __init__(self, title: str):
        """
        Inicializa una nueva instancia de la clase Exam.

        Args:
            title (str): El título del examen.
        """
        self.title = title
        self.questions = []

    def add_question(self, question):
        """
         Agrega una nueva pregunta al examen.

        Args:
            question (Question): La pregunta a agregar.
        """
        self.questions.append(question)

    def remove_question(self, index: int):
        """
        Elimina una pregunta del examen según su índice.

        Args:
            index (int): Índice de la pregunta a eliminar.

        Raises:
            ValueError: Si el índice no corresponde a ninguna pregunta existente.
        """
        try:
            del self.questions[index]
        except IndexError:
            raise ValueError(f"No question at index {index}")

    def update_question(self, index: int, new_question):
        """
         Actualiza una pregunta existente en el examen.

        Args:
            index (int): Índice de la pregunta a actualizar.
            new_question (Question): Nueva pregunta que reemplaza a la existente.

        Raises:
            ValueError: Si el índice no corresponde a ninguna pregunta existente.
        """
        try:
            self.questions[index] = new_question
        except IndexError:
            raise ValueError(f"No question at index {index}")
