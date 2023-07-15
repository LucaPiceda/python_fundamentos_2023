# Calculo de promedio
def calcular_promedio(notas):
    suma = sum(notas)
    cantidad = len(notas)
    return suma / cantidad

# Mostrar lista
def mostrar_lista_alumnos(alumnos):
    alumnos_ordenados = sorted(alumnos)
    for alumno in alumnos_ordenados:
        print(alumno[0])

# Mostrar lista con notas
def mostrar_lista_alumnos_notas(alumnos):
    alumnos_ordenados = sorted(alumnos)
    for alumno in alumnos_ordenados:
        notas = ", ".join(str(nota) for nota in alumno[1])
        print(f"{alumno[0]}: {notas}")

# Mostrar lista con promedios
def mostrar_lista_alumnos_promedios(alumnos):
    alumnos_ordenados = sorted(alumnos)
    for alumno in alumnos_ordenados:
        promedio = calcular_promedio(alumno[1])
        print(f"{alumno[0]}: Promedio = {promedio}")

# Mostrar nota media de todos
def mostrar_nota_media_todos_alumnos(alumnos):
    notas_totales = []
    cantidad_notas = 0
    for alumno in alumnos:
        for nota in alumno[1]:
            notas_totales.append(nota)
            cantidad_notas += 1
    nota_media = sum(notas_totales) / cantidad_notas
    print("Nota media de todos los alumnos: " + str(nota_media))

# Mostrar nota media de APROBADOS
def mostrar_nota_media_alumnos_aprobados(alumnos):
    notas_aprobadas = []
    cantidad_alumnos_aprobados = 0
    for alumno in alumnos:
        promedio = calcular_promedio(alumno[1])
        if promedio >= 6.0:
            notas_aprobadas.extend(alumno[1])
            cantidad_alumnos_aprobados += 1
    if cantidad_alumnos_aprobados > 0:
        nota_media_aprobados = sum(notas_aprobadas) / len(notas_aprobadas)
        print("Nota media de los alumnos aprobados: " + str(nota_media_aprobados))
    else:
        print("No hay alumnos aprobados")

# Nota media desaprobados
def mostrar_nota_media_alumnos_desaprobados(alumnos):
    notas_desaprobadas = []
    cantidad_alumnos_desaprobados = 0
    for alumno in alumnos:
        promedio = calcular_promedio(alumno[1])
        if promedio < 6.0:
            notas_desaprobadas.extend(alumno[1])
            cantidad_alumnos_desaprobados += 1
    if cantidad_alumnos_desaprobados > 0:
        nota_media_desaprobados = sum(notas_desaprobadas) / len(notas_desaprobadas)
        print("Nota media de los alumnos desaprobados: " + str(nota_media_desaprobados))
    else:
        print("No hay alumnos desaprobados")

# Función principal del programa
def main():
    print("Bienvenido al programa de gestión de alumnos")
    alumnos = []
    cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
    for i in range(cantidad_alumnos):
        print("Ingrese los datos del alumno", i + 1)
        nombre = input("Nombre completo: ")
        cantidad_notas = int(input("Cantidad de notas (entre 3 y 6): "))
        while cantidad_notas < 3 or cantidad_notas > 6:
            print("Cantidad de notas inválida. Intente nuevamente.")
            cantidad_notas = int(input("Cantidad de notas (entre 3 y 6): "))
        notas = []
        for j in range(cantidad_notas):
            nota = float(input("Nota {}: ".format(j + 1)))
            notas.append(nota)
        alumno = (nombre, notas)
        alumnos.append(alumno)

    opcion = ""
    while opcion != "g":
        print("\nMenú:")
        print("a) Mostrar la lista (alfabética) de alumnos.")
        print("b) Mostrar la lista (alfabética) de alumnos con sus notas.")
        print("c) Mostrar la lista (alfabética) de alumnos con sus promedios.")
        print("d) Mostrar la nota media de todos los alumnos.")
        print("e) Mostrar la nota media de los alumnos aprobados.")
        print("f) Mostrar la nota media de los alumnos suspendidos.")
        print("g) Salir del programa.")
        opcion = input("Seleccione una opción: ")

        if opcion == "a":
            mostrar_lista_alumnos(alumnos)
        elif opcion == "b":
            mostrar_lista_alumnos_notas(alumnos)
        elif opcion == "c":
            mostrar_lista_alumnos_promedios(alumnos)
        elif opcion == "d":
            mostrar_nota_media_todos_alumnos(alumnos)
        elif opcion == "e":
            mostrar_nota_media_alumnos_aprobados(alumnos)
        elif opcion == "f":
            mostrar_nota_media_alumnos_desaprobados(alumnos)
        elif opcion == "g":
            print("¡Hasta luego!")
        else:
            print("Opción inválida. Intente nuevamente.")

main()