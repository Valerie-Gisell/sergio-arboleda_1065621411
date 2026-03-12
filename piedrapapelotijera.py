import random

# Contadores de victorias
victorias_usuario = 0
victorias_maquina = 0

# Opciones válidas
opciones = ["piedra", "papel", "tijera"]

# Bucle principal del juego
while True:
    print("\n=== PIEDRA, PAPEL O TIJERA ===")
    print(f"Victorias - Tú: {victorias_usuario} | Máquina: {victorias_maquina}")
    
    # Pedir elección del usuario con validación
    eleccion_usuario = ""
    while eleccion_usuario not in opciones:
        eleccion_usuario = input("\nElige: piedra, papel o tijera: ").lower()
        if eleccion_usuario not in opciones:
            print("✗ Opción no válida. Intenta de nuevo.")
    
    # Elección aleatoria de la máquina
    eleccion_maquina = random.choice(opciones)
    
    # Mostrar elecciones
    print(f"\nTú elegiste: {eleccion_usuario}")
    print(f"Máquina eligió: {eleccion_maquina}")
    
    # Determinar el ganador
    if eleccion_usuario == eleccion_maquina:
        resultado = "¡Empate!"
    elif (eleccion_usuario == "piedra" and eleccion_maquina == "tijera") or \
         (eleccion_usuario == "tijera" and eleccion_maquina == "papel") or \
         (eleccion_usuario == "papel" and eleccion_maquina == "piedra"):
        resultado = "¡Ganaste!"
        victorias_usuario = victorias_usuario + 1
    else:
        resultado = "¡Perdiste!"
        victorias_maquina = victorias_maquina + 1
    
    # Mostrar resultado
    print(f"\n{resultado}")
    
    # Preguntar si quiere jugar otra vez
    jugar_otra = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_otra != "s":
        print(f"\n=== RESULTADO FINAL ===")
        print(f"Victorias - Tú: {victorias_usuario} | Máquina: {victorias_maquina}")
        if victorias_usuario > victorias_maquina:
            print("¡Felicidades! Ganaste más rondas.")
        elif victorias_maquina > victorias_usuario:
            print("La máquina ganó más rondas. ¡Suerte la próxima!")
        else:
            print("¡Fue un empate general!")
        print("\n¡Hasta luego!")
        break
