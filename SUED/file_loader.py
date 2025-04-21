import os
import pickle
from SUED.file_generator import FileGenerator
from SUED.ollama_singleton import OllamaSingleton


class FileLoader:
    """
    Clase para cargar todos los exámenes guardados en FileGenerator desde la carpeta SAVE_DIR.
    """

    def __init__(self):
        self.responses_list = self.load_all()
        self.ollama_instance = OllamaSingleton()

    @staticmethod
    def load_all():
        """Carga todos los archivos pickle en la carpeta de exámenes guardados."""
        save_dir = "RAG_15"
        if not os.path.exists(save_dir):
            print(f"La carpeta '{save_dir}' no existe. No hay archivos para cargar.")
            return []

        files = [
            pickle.load(open(entry.path, "rb"))
            for entry in os.scandir(save_dir)
            if entry.is_file() and entry.name.endswith(".pkl")
        ]

        print(f"Se cargaron {len(files)} exámenes desde '{save_dir}'.")
        return files

    def evaluate_response(self, user_answer, correct_answer):
        """Evalúa una respuesta y retorna 'correcta' o 'incorrecta'."""
        try:
            # gemma3:4b-it-q4_K_M
            print(f">>> Respuesta Correcta: {correct_answer}")
            print(f">>> Respuesta del Modelo: {user_answer}")
            result = self.ollama_instance.client.chat(
                model="gemma3:12b-it-q4_K_M",
                messages=[
                    {'role': 'system', 'content': 'Eres un asistente que califica pruebas.'},
                    {'role': 'user', 'content': f"""
                    Se obtuvieron las respuestas que un candidato proporcionó para una evaluación. Como era una 
                    evaluación de preguntas "abiertas", el candidato podría colocar cuálquier cosa:
                    
                    - Respuestas muy largas.
                    - Respuestas muy cortas.
                    - Respuestas muy contundentes.
                    - Respuestas muy extensas y con rodeos.
                    - Se puede equivocar al escribir una palabra.
                    
                    Es necesario evaluar si la respuesta del candidato concuerda (no si es idéntica) a la respuesta
                    que se tiene por correcta, pues debemos tener flexibilidad al evaluar la respuesta del candidato 
                    y determinar si lo que escribió es correcto y tiene fundamentos para relacionarse con la respuesta 
                    correcta o si simplemente no tenía idea de lo que respondía.
                    
                    Si la respuesta del candidato se considera correcta deberás retornar solamente la palabra "correcta".
                    Si la respuesta del candidato se considere incorrecta deberás retornar solamente la palabra "incorrecta".
                    
                    La respuesta correcta es: {correct_answer}
                    
                    
                    """},
                    {'role': 'user', 'content': f"La respuesta del candidato es: {user_answer}"}
                ]
            )
            print(f"\n>>> >>> La respuesta es {result['message']['content'].strip()}\n")
            return (result['message']['content'].strip()).lower()
        except Exception as e:
            print(f"Error en evaluación: {e}")
            return "error"

    def query_model(self):
        """Evalúa respuestas del usuario y calcula precisión y tiempo de respuesta."""
        data_list = []

        for response in self.responses_list:

            if response.user_responses.response_id not in ["deepseek-r1:7b-qwen-distill-q4_K_M"]:

                print(f"Evaluando respuestas de: {response.user_responses.response_id}")

                evaluaciones = [
                    (self.evaluate_response(item["user_answer"], item["correct_answer"]), item["response_time"])
                    for item in response.user_responses.responses_list
                ]

                respuestas_correctas = sum(1 for resp, _ in evaluaciones if resp == "correcta")
                total_respuestas = len(evaluaciones)

                precision = (respuestas_correctas * 100 / total_respuestas) if total_respuestas else 0
                tiempo_promedio = sum(time for _, time in evaluaciones) / total_respuestas if total_respuestas else 0

                print(f"Precisión: {precision:.2f}% | Tiempo de respuesta: {tiempo_promedio:.2f} seg")

                data_list.append({
                    "Modelo": response.user_responses.response_id,
                    "Precisión": round(precision, 2),
                    "Tiempo de Respuesta": round(tiempo_promedio, 2)
                })

        return data_list


if __name__ == "__main__":
    file_loader = FileLoader()

    for item in file_loader.query_model():
        print(item)
