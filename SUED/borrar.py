import ollama

import requests
import json


def instalar_modelo_con_progreso(modelo: str):
    url = "http://localhost:11434/api/pull"
    response = requests.post(url, json={"name": modelo}, stream=True)

    if response.status_code != 200:
        print(f"Error al iniciar la descarga del modelo {modelo}")
        return

    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8"))
                status = data.get("status")
                digest = data.get("digest", "")
                total = data.get("total", 0)
                completed = data.get("completed", 0)

                if completed and total:
                    porcentaje = (completed / total) * 100
                    print(f"{status or 'Descargando'}: {porcentaje:.2f}%")
                else:
                    print(status or data)
            except json.JSONDecodeError:
                print("No se pudo decodificar una línea del stream:", line)

    print(f"\n✅ Modelo {modelo} instalado correctamente.")


# Ejemplo de uso
#instalar_modelo_con_progreso("llama3:8b")

if __name__ == "__main__":
    print("Prueba")
    # print(ollama.delete("qwen2.5:0.5b-instruct-q3_K_S"))

    # instalar_modelo_con_progreso("qwen2.5:0.5b-instruct-q3_K_S")