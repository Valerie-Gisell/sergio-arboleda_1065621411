# ...existing code...
import random

TOTAL_ESTUDIANTES = 5

nombres_disponibles = ["Ana", "Luis", "María", "Carlos", "Sofía", "Juan", "Lucía", "Diego", "Valeria", "Mateo"]
nombres = random.sample(nombres_disponibles, TOTAL_ESTUDIANTES)

total_calificaciones = 0.0
mejor_nombre = None
mejor_calificacion = -1.0
peor_nombre = None
peor_calificacion = 999.0

print("Estudiantes generados:")
for i, nombre in enumerate(nombres, 1):
    edad = random.randint(5, 100)               # edad entre 5 y 100
    calificacion = round(random.uniform(0, 5), 1)  # calificación entre 0 y 5 con 1 decimal
    print(f"{i}. {nombre} - Edad: {edad}, Calificación: {calificacion}")

    total_calificaciones += calificacion
    if calificacion > mejor_calificacion:
        mejor_calificacion = calificacion
        mejor_nombre = nombre
    if calificacion < peor_calificacion:
        peor_calificacion = calificacion
        peor_nombre = nombre

promedio = total_calificaciones / TOTAL_ESTUDIANTES

print("\nResultados:")
print(f"Mejor estudiante: {mejor_nombre} con calificación {mejor_calificacion:.1f}")
print(f"Peor estudiante: {peor_nombre} con calificación {peor_calificacion:.1f}")
print(f"Calificación promedio: {promedio:.2f}")
# ...existing code...