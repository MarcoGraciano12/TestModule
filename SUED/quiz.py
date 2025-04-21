"""

"""
# Importación de módulos.
from SUED.quiz_item import QuizItem

# Declaración de clases.
class Quiz:

    def __init__(self, quiz_name:str):
        self.quiz_name = quiz_name
        self.quiz_item_list = []

    def add_quiz_item(self, question:str, answer:str):
        # Se instancia un objeto de la case QuizItem
        new_quiz_item = QuizItem(question=question, answer=answer)
        # Se añade el objeto a la lista
        self.quiz_item_list.append(new_quiz_item)

    def __str__(self):
        return f"Quiz Name: {self.quiz_name} | Quiz Items: {[item.__str__() for item in self.quiz_item_list]}"

# Ejemplo de implementación.
if __name__ == "__main__":
    # Se instancia un objeto de la clase Quiz
    quiz = Quiz("Español")

    print(f"Nombre de la prueba: {quiz.quiz_name}")

    # Agregar un elemento a la lista de preguntas
    quiz.add_quiz_item("¿De qué color es el cielo?", "Azul")

    # Mostrar el contenido de la lista de preguntas
    print(quiz)