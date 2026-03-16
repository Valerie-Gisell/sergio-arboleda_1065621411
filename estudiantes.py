import re

def validar_cedula(cedula):
    return cedula.isdigit() and 8 <= len(cedula) <= 10


def validar_email(email):
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(patron, email) is not None


def validar_calificaciones(calificaciones):
    for nota in calificaciones:
        if nota < 0 or nota > 5:
            return False
    return True


def calcular_promedio(calificaciones):
    return round(sum(calificaciones) / len(calificaciones), 2)


def clasificar_desempeño(promedio):
    if promedio >= 4.5:
        return "Excelente"
    elif promedio >= 4.0:
        return "Muy bueno"
    elif promedio >= 3.5:
        return "Bueno"
    elif promedio >= 3.0:
        return "Satisfactorio"
    else:
        return "Necesita mejorar"


def crear_estudiante(cedula, nombre, email, calificaciones):
    if not validar_cedula(cedula):
        print("Cédula inválida.")
        return None

    if not validar_email(email):
        print("Email inválido.")
        return None

    if not validar_calificaciones(calificaciones):
        print("Calificaciones inválidas.")
        return None

    promedio = calcular_promedio(calificaciones)

    return {
        "cedula": cedula,
        "nombre": nombre,
        "email": email,
        "promedio": promedio
    }


def listar_estudiantes(lista_estudiantes):
    print("\nCédula | Nombre | Promedio | Desempeño")
    print("-" * 45)

    for est in lista_estudiantes:
        desempeño = clasificar_desempeño(est["promedio"])
        print(f"{est['cedula']} | {est['nombre']} | {est['promedio']} | {desempeño}")


def buscar_estudiante(lista_estudiantes, cedula):
    for est in lista_estudiantes:
        if est["cedula"] == cedula:
            desempeño = clasificar_desempeño(est["promedio"])
            print(f"{est['nombre']} | Promedio: {est['promedio']} | Desempeño: {desempeño}")
            return
    print("Estudiante no encontrado.")


def main():
    estudiantes = []

    while True:
        print("\n--- SISTEMA DE GESTIÓN DE ESTUDIANTES ---")
        print("1. Agregar estudiante")
        print("2. Ver lista de estudiantes")
        print("3. Buscar estudiante por cédula")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            email = input("Email: ")

            notas_input = input("Calificaciones (separadas por coma): ")
            try:
                calificaciones = [float(n) for n in notas_input.split(",")]
            except:
                print("Formato de calificaciones incorrecto.")
                continue

            estudiante = crear_estudiante(cedula, nombre, email, calificaciones)

            if estudiante:
                estudiantes.append(estudiante)
                desempeño = clasificar_desempeño(estudiante["promedio"])
                print(f"Estudiante agregado exitosamente. Promedio: {estudiante['promedio']} | Desempeño: {desempeño}")

        elif opcion == "2":
            if estudiantes:
                listar_estudiantes(estudiantes)
            else:
                print("No hay estudiantes registrados.")

        elif opcion == "3":
            cedula = input("Cédula a buscar: ")
            buscar_estudiante(estudiantes, cedula)

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


main()