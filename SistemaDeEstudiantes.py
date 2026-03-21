import json

# esto es solo para ensayar modificaciones


def pedirEdad():
    while True:
        try:
            edad = int(input("Ingrese la Edad: "))
            if edad > 0:
                return edad
            else:
                print("Error. Edad Invalida. Ingrese una edad Correcta")

        except ValueError:
            print("Error: Ingrese un número entero válido.")
            

def nota(numero):
    while True:
        try:
            nota = float(input(f"Ingrese la nota No. {numero}: "))
            if 0 <= nota <= 5:
                return nota
            else:
                print("Ha Ingresado una nota no valida")

        except ValueError:
            print("Error: ingrese un número válido.")


def registroEstudiante():
    nombre = input("Ingrese nombre del Estudiante: ")
    edad = pedirEdad()
    nota1 = nota(1)
    nota2 = nota(2)
    nota3 = nota(3)

    return nombre, edad, nota1, nota2, nota3

def calcularPromedio(n1, n2, n3):
    return (n1 + n2 + n3)/3

def evaluarEstado(promedio):
    if promedio >= 4.0:
        return "Aprobado"
    elif promedio >= 3.0:
        return "En Recuperacion"
    else:
        return "No Aprobado"

def inicio():

    estudiantesRegistrados = 0
    sumaPromedio = 0
    listaEstudiantes = []

    while True:
        print("\n===== SISTEMA DE ESTUDIANTES =====")
        print("1. Registrar estudiante")
        print("2. Salir")

        op = input("Seleccione una opcion: ")

        if op == "1":
            nombre, edad, n1, n2, n3 = registroEstudiante()
            promedio = calcularPromedio(n1, n2, n3)
            estado = evaluarEstado(promedio)

            estudiantesRegistrados += 1
            sumaPromedio += promedio
            listaEstudiantes.append((nombre, edad, n1, n2, n3, promedio, estado))

            print("\n===== RESULTADO DEL ESTUDIANTE =====")
            for estudiante in listaEstudiantes:
                print(f"\nNombre: {estudiante[0]}")
                print(f"Edad: {estudiante[1]}")
                print(f"Nota 1: {estudiante[2]}")
                print(f"Nota 2: {estudiante[3]}")
                print(f"Nota 3: {estudiante[4]}")
                print(f"Promedio: {estudiante[5]:.2f}")
                print(f"Estado académico: {estudiante[6]}")

        elif op == "2":
            print("\n===== RESUMEN FINAL =====")
            print(f"Total de estudiantes registrados: {estudiantesRegistrados}")

            if estudiantesRegistrados > 0:
                promedio_general = sumaPromedio / estudiantesRegistrados
                print(f"Promedio general del grupo: {promedio_general:.2f}")
                print(json.dumps(listaEstudiantes, indent=4))
            else:
                print("Promedio general del grupo: 0.00")

            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

inicio()