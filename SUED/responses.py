"""

"""
# Importación de Módulos


# Definición de Clases
class Responses:

    def __init__(self, response_id: str):
        self.response_id = response_id
        self.responses_list = []

    def add_response(self, correct_answer: str, user_answer: str, response_time: float):
        # Se colocan los datos en un diccionario
        response_dict = {
            "correct_answer": correct_answer,
            "user_answer": user_answer,
            "response_time": response_time
        }

        # Se agrega el diccionario a la lista de respuestas
        self.responses_list.append(response_dict)


    def __str__(self):

        string = "\n--* ".join([(f"Correct Answer: {response["correct_answer"]} | "
                   f"User Answer: {response["user_answer"]} | "
                   f"Response Time: {response["response_time"]}") for response in self.responses_list])



        return f"ID:\n--* {self.response_id}\nResponses:\n--* {string}"



# Ejemplo de Implementación
if __name__ == "__main__":

    # Se instancia un objeto de la clase Responses
    responses = Responses("1234")

    # Se agregan preguntas a la lista de respuestas del usuario
    responses.add_response("Azul", "Verde", 3.2)
    responses.add_response("Cuatro", "Cinco", 2.5)

    # Mostrar los atributos del objeto
    print(responses)