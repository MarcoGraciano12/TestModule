"""

"""
# Importación de Módulos
from quiz import Quiz
from responses import Responses
import requests
import time
import pickle
import os


from exam_system.db import init_db, SessionLocal
from exam_system.domain import ExamManager

from IDGenerator import generate_id


# Variables Globales
BASE_URL="http://localhost:5000"


def get_models():
    """
    Método para obtener la lista de modelos disponibles que se encuentran en local.
    :return: un diccionario con la respuesta del endpoint.
    """
    url = f"{BASE_URL}/models"
    response = requests.get(url)
    return response.json()

def get_active_model():
    """
    Método para obtener el modelo activo.
    :return: Un diccionario con la respuesta del endpoint.
    """
    url = f"{BASE_URL}/model"
    response = requests.get(url)
    return response.json()

def set_model(index: int):
    """
    Método para establecer el modelo activo del chat.
    :param index: Indice que corresponde a la ubicación del modelo en la lista de modelos disponibles.
    :return: La respuesta del endpoint.
    """
    url = f"{BASE_URL}/model"
    data = {"index": index}
    response = requests.post(url, json=data)
    return response.json()

def set_collection(category: str):
    """
    Método para establecer el entrenamiento activo del chat.
    :param category: Nombre del entrenamiento.
    :return: Un diccionario con la respuesta del endpoint.
    """
    url = f"{BASE_URL}/collection"
    data = {"category": category}
    response = requests.post(url, json=data)
    return response.json()

def set_rag_k(k):
    """
    Método para establecer el nivel de precisión de la respuesta del modelo.
    :param k: Número de coincidencias que el rag proporcionará al modelo como contexto.
    :return: un diccionario con la respuesta del endpoint.
    """
    url = f"{BASE_URL}/rag-k"
    data = {"k": k}
    response = requests.post(url, json=data)
    return response.json()

def set_response_level(level: int):
    """
    Método para establecer el nivel de calidad de la respuesta del modelo.
    :param level: Nivel de calidad de la respuesta del modelo.
    :return:
    """
    url = f"{BASE_URL}/level"
    data = {"level": level}
    response = requests.post(url, json=data)
    return response.json()

def warmup_model():
    """
    Envía una consulta inicial para cargar el modelo antes de iniciar las preguntas reales.
    """
    print("Inicializando modelo...")
    _, time_to_first, total_time = query_model("Hola")
    print(f"Modelo cargado. Tiempo hasta la primera respuesta: {time_to_first:.2f} segundos")
    print(f"Tiempo total de carga: {total_time:.2f} segundos")

def query_model(query):
    """
    Método para realizar una consulta al modelo.
    :param query: Pregunta al modelo.
    :return: Un tuple con la respuesta del modelo, tiempo hasta la primera respuesta y tiempo total.
    """
    url = f"{BASE_URL}/ollama/chat"
    data = {"query": query}

    start_time = time.perf_counter()  # Usa `perf_counter()` para mayor precisión
    first_chunk_time = None
    response_chunks = []  # Usamos una lista en lugar de `+=`

    with requests.post(url, json=data, stream=True, timeout=35) as response:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                if first_chunk_time is None:
                    first_chunk_time = time.perf_counter()  # Más preciso que `time.time()`
                response_chunks.append(chunk.decode())  # Mejor rendimiento

    end_time = time.perf_counter()

    # Unimos los fragmentos en una sola operación eficiente
    response_text = "".join(response_chunks)

    time_to_first_token = (first_chunk_time - start_time) if first_chunk_time else (end_time - start_time)
    total_response_time = end_time - start_time

    return response_text, time_to_first_token, total_response_time

# Declaración de Clases
class FileGenerator:
    SAVE_DIR = "RAG_15"  # Carpeta donde se guardarán los archivos

    def __init__(self, response_id: str):

        self.user_responses = Responses(response_id)    # Instancia para las respuestas del LLM

        self.quiz = Quiz("Evaluación de Desempeño")     # Instancia para las preguntas de la evaluación

    def __str__(self):
        return f"Responses {self.user_responses} | Quiz: {self.quiz}"

    def save_to_file(self, filename: str):
        """
        Guarda la instancia del objeto en un archivo dentro de la carpeta SAVE_DIR usando pickle.
        Si la carpeta no existe, la crea automáticamente.
        :param filename: Nombre del archivo sin extensión.
        """
        # Crear la carpeta si no existe
        os.makedirs(self.SAVE_DIR, exist_ok=True)

        # Ruta completa del archivo
        filepath = os.path.join(self.SAVE_DIR, f"{filename}.pkl")

        # Guardar el objeto
        with open(filepath, "wb") as f:
            pickle.dump(self, f)

        print(f"Archivo guardado en: {filepath}")

    @classmethod
    def load_from_file(cls, filename: str):
        """
        Carga una instancia de FileGenerator desde un archivo pickle en SAVE_DIR.
        :param filename: Nombre del archivo sin extensión.
        :return: Instancia de FileGenerator cargada desde el archivo.
        """
        filepath = os.path.join(cls.SAVE_DIR, f"{filename}.pkl")

        # Verificar si el archivo existe antes de intentar cargarlo
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"El archivo '{filepath}' no existe.")

        with open(filepath, "rb") as f:
            obj = pickle.load(f)

        print(f"Archivo cargado desde: {filepath}")
        return obj



# Ejemplo de Implementación
if __name__ == "__main__":
    # Obtener la lista de los modelos de Ollama
    llm_list = get_models()["content"]
    for index, item in enumerate(llm_list):
        print(f"{index}) {item}")

    print(llm_list)

    # Se selecciona al modelo a evaluar
    index = 0
    llm = {"index":index, "llm_name":llm_list[index]}

    print(llm)

    # Se llenan las preguntas de la prueba de manera manual
    responses_file = FileGenerator(llm["llm_name"])


    # Se configura la respuesta del modelo
    print(set_model(llm["index"]))# Se activa el modelo
    print(set_collection("Grupo Fórmula"))   # Se indica el entrenamiento
    print(set_rag_k(15))   # Se indica la cantidad de recuperaciones de incrustaciones

    # Hacer la consulta de calentamiento
    warmup_model()

    init_db()
    session = SessionLocal()

    try:
        manager = ExamManager(session)

        exams = manager.list_exams()
        for ex in exams:
            print(f"Exam ID: {ex.id}, Title: {ex.title}, Questions: {len(ex.questions)}")
            for q in ex.questions:
                print(f"  - Q{q.id}: {q.prompt} → {q.answer}")
                response, time_to_first, total_time = query_model(q.prompt)
                print(f"--- ---* Respuesta = {response}")
                print(f"--- ---* Tiempo hasta la primera palabra: {time_to_first:.2f} segundos")
                print(f"--- ---* Tiempo total de respuesta: {total_time:.2f} segundos")

                # Se añaden las respuestas a la lista de respuestas del llm
                responses_file.user_responses.add_response(q.answer, response, time_to_first)

            # Se muestran los datos obtenidos de la prueba
            print(responses_file.user_responses)

            # Se guardan los resultados del modelo
            responses_file.save_to_file(f'{llm['index']}-RAG15')


    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        session.close()
