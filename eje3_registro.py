import os

def fnt_limpiar_pantalla():
    os.system('cls')

estudiantes = {}


def registrar_el_estudiante():
    nombre = input('Ingresar el nombre del estudiante -> ')
    edad = int(input('Ingresar la edad del estudiante -> '))
    carrera = input('Ingresar la carrera que pertenece el estudiante -> ')
    estudiantes[nombre] = {"edad": edad, "carrera": carrera}
    fnt_limpiar_pantalla()

def buscar_estudiante():
    nombre = input("Ingresa el nombre del estudiante a buscar: ")
    if nombre in estudiantes:
        print(f"El estudiante {nombre} tiene {estudiantes[nombre]['edad']} años de edad y estudia la carrera {estudiantes[nombre]['carrera']}.")
        enter = input('\n<<<ENTER>>>')
        fnt_limpiar_pantalla()
    else:
        print(' El estudiante mencionado no se encuentra registrado ')
        enter = input('\n<<<ENTER>>>')
        fnt_limpiar_pantalla()



while True:
    print('<<< MENU DE OPCIONES >>>')
    print('1. Registrar estudiante')
    print('2. Buscar estudiante')
    print('3. Salir')
    opcion = int(input('Elige una opción: '))

    if opcion == 1:
        registrar_el_estudiante()
    elif opcion == 2:
        buscar_estudiante()
    elif opcion == 3:
        break
    else:
        print('<<<ERROR>>> intenta de nuevo')
        enter = input('\n<<<ENTER>>>')
        fnt_limpiar_pantalla()




