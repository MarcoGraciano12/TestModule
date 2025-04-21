"""
Clase que representa una pregunta simple.

Esta clase encapsula el enunciado de una pregunta (`prompt`) y su respuesta (`answer`).
Puede ser utilizada para representar preguntas de manera independiente al modelo de base de datos.
"""
class Question:
    """
     Representa una pregunta con su enunciado y respuesta.
    """
    def __init__(self, prompt: str, answer: str):
        """
        Inicializa una nueva instancia de la clase Question.

        Args:
            prompt (str): El enunciado o contenido de la pregunta.
            answer (str): La respuesta correcta asociada a la pregunta.
        """
        self.prompt = prompt
        self.answer = answer
