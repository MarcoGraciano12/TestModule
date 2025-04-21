import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lista de diccionarios
datos = [
    {'Modelo': 'llama3.2:3b-instruct-q3_K_S', 'Precisión': 64.29, 'Tiempo de Respuesta': 8.88},
    {'Modelo': 'llama3.2:3b-instruct-q4_K_S', 'Precisión': 71.43, 'Tiempo de Respuesta': 7.28},
    {'Modelo': 'qwen2.5:0.5b-instruct-q4_K_S', 'Precisión': 50.0, 'Tiempo de Respuesta': 1.21},
    {'Modelo': 'gemma2:2b-instruct-q4_K_M', 'Precisión': 78.57, 'Tiempo de Respuesta': 4.41},
    {'Modelo': 'qwen2.5:1.5b-instruct-q4_K_M', 'Precisión': 64.29, 'Tiempo de Respuesta': 3.5},
    {'Modelo': 'llama3.2:3b-instruct-q4_K_M', 'Precisión': 78.57, 'Tiempo de Respuesta': 7.53},
    {'Modelo': 'qwen:1.8b-chat-fp16', 'Precisión': 78.57, 'Tiempo de Respuesta': 3.0},
    {'Modelo': 'qwen2.5:3b-instruct-q8_0', 'Precisión': 78.57, 'Tiempo de Respuesta': 6.8},
    {'Modelo': 'qwen2.5:1.5b-instruct-fp16', 'Precisión': 71.43, 'Tiempo de Respuesta': 3.16},
    {'Modelo': 'llama3:8b-instruct-q4_K_S', 'Precisión': 78.57, 'Tiempo de Respuesta': 17.88},
    {'Modelo': 'llama3.2:3b-instruct-fp16', 'Precisión': 71.43, 'Tiempo de Respuesta': 7.09},
    {'Modelo': 'deepseek-r1:1.5b-qwen-distill-q8_0', 'Precisión': 35.71, 'Tiempo de Respuesta': 2.95},
    {'Modelo': 'gemma3:4b-it-q4_K_M', 'Precisión': 78.57, 'Tiempo de Respuesta': 6.99},
    {'Modelo': 'gemma2:2b-instruct-q8_0', 'Precisión': 78.57, 'Tiempo de Respuesta': 3.7},
    {'Modelo': 'gemma:2b-instruct-v1.1-fp16', 'Precisión': 71.43, 'Tiempo de Respuesta': 4.16},
    {'Modelo': 'qwen:1.8b-chat-fp16', 'Precisión': 50.0, 'Tiempo de Respuesta': 3.14},
    {'Modelo': 'qwen2.5:3b', 'Precisión': 85.71, 'Tiempo de Respuesta': 7.52},
    {'Modelo': 'qwen2.5:1.5b', 'Precisión': 64.29, 'Tiempo de Respuesta': 3.5},
    {'Modelo': 'qwen2.5:0.5b', 'Precisión': 64.29, 'Tiempo de Respuesta': 1.17},
    {'Modelo': 'llama3.1:8b', 'Precisión': 78.57, 'Tiempo de Respuesta': 18.52},
    {'Modelo': 'llama3.2:1b', 'Precisión': 71.43, 'Tiempo de Respuesta': 2.03},
    {'Modelo': 'deepseek-r1:7b-qwen-distill-q4_K_M', 'Precisión': 71.43, 'Tiempo de Respuesta': 17.35},
    {'Modelo': 'deepseek-r1:1.5b-qwen-distill-fp16', 'Precisión': 42.86, 'Tiempo de Respuesta': 3.43},
    {'Modelo': 'phi4-mini:latest', 'Precisión': 78.57, 'Tiempo de Respuesta': 7.35}
]

if __name__ == "__main__":
    # Convertir a DataFrame
    df = pd.DataFrame(datos)

    print(df)

    # Extraer la familia del modelo (Llama, Gemma, Qwen, Deepseek)
    df["Grupo"] = df["Modelo"].str.extract(r"^(llama|gemma|qwen|deepseek|phi)")

    # Configuración del gráfico
    sns.set(style="whitegrid")

    # Crear la figura
    plt.figure(figsize=(10, 6))

    # Crear un swarmplot manual con scatterplot para asegurar que la leyenda funcione
    for grupo in df["Grupo"].unique():
        subset = df[df["Grupo"] == grupo]
        sns.scatterplot(x=subset["Grupo"], y=subset["Precisión"], label=grupo, s=100)

    # Configuración de etiquetas y título
    plt.xlabel("Familia del Modelo")
    plt.ylabel("Precisión")
    plt.title("Distribución de Precisión por Familia de Modelos")

    # Ajustar la escala del eje Y de 0 a 100
    plt.ylim(0, 100)

    # Mostrar la leyenda correctamente
    plt.legend(title="Familia del Modelo")

    # Mostrar gráfico
    plt.show()

    # ____________________________________________________

    # Crear la figura
    plt.figure(figsize=(10, 6))

    # Crear scatterplot para mostrar los modelos en función de su precisión y tiempo de respuesta
    sns.scatterplot(x="Tiempo de Respuesta", y="Precisión", data=df, hue="Modelo", palette="deep", s=100)

    # Configuración de etiquetas y título
    plt.xlabel("Tiempo de Respuesta")
    plt.ylabel("Precisión")
    plt.title("Precisión vs. Tiempo de Respuesta por Modelo")

    # Mostrar la leyenda
    plt.legend(title="Modelo", bbox_to_anchor=(1.05, 1), loc='upper left')

    # Mostrar gráfico
    plt.tight_layout()
    plt.show()

    # ____________________________________________________

    # Crear la figura
    plt.figure(figsize=(12, 8))

    # Crear colores para las barras usando una paleta diferente
    # Spectral
    colors = sns.color_palette("magma", n_colors=len(df))  # Otra paleta, puedes cambiar "Set3" por otra

    # Crear gráfico de barras
    bars = plt.bar(df["Modelo"], df["Tiempo de Respuesta"], color=colors)

    # Rotar las etiquetas de los modelos
    plt.xticks(rotation=90)

    # Quitar las etiquetas del eje X (sin los nombres de los modelos)
    plt.xticks([])  # Esto elimina las etiquetas del eje X

    # Configuración de etiquetas y título
    plt.xlabel("Modelo")
    plt.ylabel("Tiempo de Respuesta")
    plt.title("Tiempo de Respuesta por Modelo")

    # Crear leyenda con los colores correspondientes a los modelos
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in colors]
    plt.legend(handles, df["Modelo"], title="Modelo", bbox_to_anchor=(1.05, 1), loc='upper left')

    # Mostrar gráfico
    plt.tight_layout()
    plt.show()

    # _____________________________________________________

    # Crear la figura
    plt.figure(figsize=(8, 6))

    # Crear colores para las barras usando una paleta diferente
    # Spectral
    colors = sns.color_palette("Spectral", n_colors=len(df))  # Otra paleta, puedes cambiar "Set3" por otra

    # Crear gráfico de barras
    bars = plt.bar(df["Modelo"], df["Precisión"], color=colors)

    # Rotar las etiquetas de los modelos
    plt.xticks(rotation=90)

    # Quitar las etiquetas del eje X (sin los nombres de los modelos)
    plt.xticks([])  # Esto elimina las etiquetas del eje X

    # Configuración de etiquetas y título
    plt.xlabel("Modelo")
    plt.ylabel("Precisión")
    plt.title("Precisión por Modelo")

    # Crear leyenda con los colores correspondientes a los modelos
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in colors]
    plt.legend(handles, df["Modelo"], title="Modelo", bbox_to_anchor=(1.05, 1), loc='upper left')

    # Mostrar gráfico
    plt.tight_layout()
    plt.show()
