# main.py

import ahorcado_diagramas
import palabras

class JuegoAhorcado:
    def __init__(self):
        """Inicializa los atributos del juego."""
        self.palabra_secreta = palabras.obtener_palabra()
        self.palabra_adivinada = ['_'] * len(self.palabra_secreta)
        self.intentos_fallidos = 0
        self.letras_usadas = []

    def mostrar_estado_juego(self):
        """Muestra el estado actual del juego."""
        print(ahorcado_diagramas.obtener_diagrama(self.intentos_fallidos))
        print("Palabra: " + " ".join(self.palabra_adivinada))
        print(f"Letras usadas: {', '.join(self.letras_usadas)}")
        print(f"Intentos restantes: {6 - self.intentos_fallidos}\n")

    def adivinar(self, letra):
        """Procesa la letra ingresada por el usuario."""
        if letra in self.letras_usadas:
            print("Ya has usado esa letra. Intenta con otra.")
            return
        self.letras_usadas.append(letra)

        if letra in self.palabra_secreta:
            for i, char in enumerate(self.palabra_secreta):
                if char == letra:
                    self.palabra_adivinada[i] = letra
        else:
            self.intentos_fallidos += 1

    def jugar(self):
        """Controla la lógica del juego."""
        print("¡Bienvenido al juego del Ahorcado!\n")
        while self.intentos_fallidos < 6 and '_' in self.palabra_adivinada:
            self.mostrar_estado_juego()
            letra = input("Adivina una letra: ").lower()
            if len(letra) != 1 or not letra.isalpha():
                print("Por favor, introduce una sola letra.\n")
                continue
            self.adivinar(letra)

        if '_' not in self.palabra_adivinada:
            print("¡Felicidades! Has adivinado la palabra: " + self.palabra_secreta)
        else:
            self.mostrar_estado_juego()
            print("Has perdido. La palabra era: " + self.palabra_secreta)

if __name__ == "__main__":
    juego = JuegoAhorcado()
    juego.jugar()
