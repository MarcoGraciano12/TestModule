"""

"""
# Importación de módulos.


# Definición de clases.
class QuizItem:

    def __init__(self, question:str, answer:str):
        self.question = question
        self.answer = answer

    def __str__(self):
        return f"Question: {self.question} | Answer: {self.answer}"




# Ejemplo de implementación.
if __name__ == "__main__":
    # Se instancia un objeto de la clase QuizItem
    quiz_item = QuizItem(question="¿De qué color es el cielo?", answer="Verde")

    # Mostrar los atributos del objeto
    print(f"question: {quiz_item.question}")
    print(f"answer: {quiz_item.answer}")