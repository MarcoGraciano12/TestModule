"""

"""
# Importación de módulos
import uuid
# Declaración de clases

# Declaración de métodos
def generate_id(length: int) -> str:
    # Generar un UUID versión 4 (aleatorio)
    unique_id = uuid.uuid4()

    # Convertir el UUID a una cadena de caracteres hexadecimal
    hex_id = unique_id.hex

    # Ajustar la longitud de la cadena según lo que desee el usuario
    if length > len(hex_id):
        raise ValueError(f"La longitud máxima permitida es {len(hex_id)} caracteres.")

    return hex_id[:length]

if __name__ == "__main__":
    # Ejemplo de uso

    # Generación de un identificador de 5 carácteres
    new_id = generate_id(5)
    print(new_id)
    # Generación de un identificador de 8 carácteres
    new_id = generate_id(8)
    print(new_id)