# palabras.py

# Lista de palabras para el juego del ahorcado
PALABRAS = [
    "python",
    "programacion",
    "desarrollador",
    "ahorcado",
    "computadora",
    "juego",
    "tecnologia"
]

def obtener_palabra():
    """Función que selecciona y devuelve una palabra aleatoria de la lista de palabras."""
    import random
    return random.choice(PALABRAS)
