# Cajero Automático
saldo = 1000

# Bucle infinito
while True:
    # Mostrar menú
    print("\n=== CAJERO AUTOMÁTICO ===")
    print("1. Ver saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    
    # Pedir opción al usuario
    opcion = input("\nElige una opción (1-4): ")
    
    # Opción 1: Ver saldo
    if opcion == "1":
        print(f"\nTu saldo es: ${saldo}")
    
    # Opción 2: Depositar
    elif opcion == "2":
        monto = float(input("¿Cuánto dinero deseas depositar? $"))
        if monto > 0:
            saldo = saldo + monto
            print(f"✓ Depósito exitoso. Nuevo saldo: ${saldo}")
        else:
            print("✗ El monto debe ser mayor a 0")
    
    # Opción 3: Retirar
    elif opcion == "3":
        monto = float(input("¿Cuánto dinero deseas retirar? $"))
        
        # Validar que haya suficiente saldo
        if monto > saldo:
            print(f"✗ Saldo insuficiente. Tu saldo es: ${saldo}")
        elif monto > 0:
            saldo = saldo - monto
            print(f"✓ Retiro exitoso. Nuevo saldo: ${saldo}")
        else:
            print("✗ El monto debe ser mayor a 0")
    
    # Opción 4: Salir
    elif opcion == "4":
        print(f"\n¡Hasta luego! Tu saldo final es: ${saldo}")
        break
    
    # Opción inválida
    else:
        print("✗ Opción no válida. Intenta de nuevo")
