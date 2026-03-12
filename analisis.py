# Programa de análisis de números
print("=== ANÁLISIS DE NÚMEROS ===")
print("Ingresa números uno por uno. Escribe 0 para terminar.")

# Inicializar variables
contador = 0
suma = 0
mayor = None
menor = None
pares = 0
impares = 0

# Bucle para pedir números
while True:
    numero = input("Ingresa un número: ")
    
    # Validar que sea un número
    if numero.isdigit() or (numero.startswith('-') and numero[1:].isdigit()):
        numero = int(numero)
        
        # Si es 0, salir del bucle
        if numero == 0:
            break
        
        # Contar el número
        contador = contador + 1
        
        # Sumar
        suma = suma + numero
        
        # Determinar mayor y menor
        if mayor is None or numero > mayor:
            mayor = numero
        if menor is None or numero < menor:
            menor = numero
        
        # Contar pares e impares
        if numero % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1
    else:
        print("✗ Debes ingresar un número válido")

# Mostrar resultados si se ingresaron números
if contador > 0:
    promedio = suma / contador
    print(f"\n=== RESULTADOS ===")
    print(f"Cantidad total de números: {contador}")
    print(f"Suma total: {suma}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Número mayor: {mayor}")
    print(f"Número menor: {menor}")
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
else:
    print("\nNo se ingresaron números válidos.")
