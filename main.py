import random

# Diccionario de opciones de juego
opciones = {'piedra': 'tijera', 'papel': 'piedra', 'tijera': 'papel'}

# Bucle principal del juego
while True:
    # Obtener la elección del jugador
    eleccion_jugador = input("Elige piedra, papel o tijera: ")
    # Obtener la elección de la computadora
    eleccion_computadora = random.choice(list(opciones.keys()))
    # Imprimir las elecciones
    print("Jugador eligió: " + eleccion_jugador)
    print("Computadora eligió: " + eleccion_computadora)
    # Comprobar quién gana
    if eleccion_jugador == eleccion_computadora:
        print("Empate!")
    elif opciones[eleccion_jugador] == eleccion_computadora:
        print("Ganaste!")
    else:
        print("Perdiste!")
    # Preguntar al jugador si desea jugar de nuevo
    continuar = input("¿Quieres jugar de nuevo? (s/n) ")
    if continuar.lower() != 's':
        break
        