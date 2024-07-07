import os
import tabulate
import time
lista_alumnos = [
              {
                  'nombre':'yessica zegarra',
                  'email': 'yessizegarrav@hotmail.com',
                  'celular':'954079097'
              }
              ]
ANCHO =50
opcion = 0
while(opcion < 5):
    os.system("clear")
    print("="*ANCHO)
    print(" " * 10 + "CRUD DE ALUMNOS")
    print("="*ANCHO)
    print("""
          [1] REGISTRAR ALUMNO
          [2] MOSTRAR ALUMNO
          [3] ACTUALIZAR ALUMNO
          [4] ELIMINAR ALUMNO 
          [5] SALIR
    """)
    print("="*ANCHO)
    opcion = int(input("INGRESE LA OPCION : "))
    os.system("clear")
    if(opcion == 1):
        print("="*ANCHO)
        print(" "*10 + "[1] REGISTRAR ALUMNO")
        print("="*ANCHO)
        nombre = input("NOMBRE: ")
        email = input("E MAIL: ")
        celular = input("celular: ")
        dic_nuevo_alumno = {
            'nombre':nombre,
            'email':email,
            'celular':celular
        }
        lista_alumnos.append(dic_nuevo_alumno)
        print("ALUMNO REGISTRADO CON EXITO")
    elif (opcion == 2):
        print("="*ANCHO)
        print(" "*10 + "[2] MOSTRAR ALUMNO")
        print("="*ANCHO)
        cabeceras = ["NOMBRE", "EMAIL","CELULAR"]
        tabla = [alumno.values() for alumno in lista_alumnos]
        print(tabulate.tabulate(tabla,headers=cabeceras,tablefmt="grid"))
        input("presiona ENTER para continuar...")
    elif (opcion == 3):
        print("="*ANCHO)
        print(" "*10 + "[3] ACTUALIZAR ALUMNO")
        print("="*ANCHO)
    elif (opcion == 4):
        print("="*ANCHO)
        print(" "*10 + "[4] ELIMINAR ALUMNO")
        print("="*ANCHO)
    elif (opcion == 5):
        print("="*ANCHO)
        print(" "*10 + "[5] SALIR")
        print("="*ANCHO)
    else:
        print("="*ANCHO)
        print(" "*10 + "OPCION INVALIDA")
        print("="*ANCHO)
    time.sleep(1)