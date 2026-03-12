import random

# Definir los caracteres disponibles
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
especiales = "!@#$%"

# Combinar todos los caracteres
todos_caracteres = mayusculas + minusculas + numeros + especiales

# Bucle infinito principal
while True:
    print("\n=== GENERADOR DE CONTRASEÑAS ===")
    
    # Bucle infinito para validar la longitud
    longitud_valida = False
    while longitud_valida == False:
        longitud = input("¿Cuál es la longitud de la contraseña? (8-20): ")
        
        # Condicional: Validar que sea un número
        if longitud.isdigit():
            longitud = int(longitud)
            
            # Condicional: Validar el rango
            if longitud >= 8 and longitud <= 20:
                longitud_valida = True
            else:
                print("✗ La longitud debe estar entre 8 y 20 caracteres")
        else:
            print("✗ Debes ingresar un número válido")
    
    # Generar la contraseña
    contraseña = ""
    for i in range(longitud):
        contraseña = contraseña + random.choice(todos_caracteres)
    
    # Mostrar la contraseña
    print(f"\n✓ Contraseña generada: {contraseña}")
    
    # Preguntar si quiere generar otra
    respuesta = input("\n¿Deseas generar otra contraseña? (s/n): ").lower()
    
    # Condicional: Si no es 's', salir del bucle infinito
    if respuesta != "s":
        print("\n¡Hasta luego!")
        break
