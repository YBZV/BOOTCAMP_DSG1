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
ANCHO = 50
opcion = 0
def mostrar_menu(ancho):
    print("="*ancho)
    print(" " * 10 + "CRUD DE ALUMNOS")
    print("="*ancho)
    print("""
          [1] REGISTRAR ALUMNO
          [2] MOSTRAR ALUMNO
          [3] ACTUALIZAR ALUMNO
          [4] ELIMINAR ALUMNO 
          [5] SALIR
    """)
    print("="*ancho)
def buscar_alumnos(valor_busqueda,listado):
    posicion_busqueda = -1
    for posicion in range(len(lista_alumnos)):
            dic_alumno = lista_alumnos[posicion]
            if valor_busqueda in dic_alumno.values():
               posicion_busqueda = posicion
               break
    return posicion_busqueda
while(opcion < 5):
    os.system("clear")
    mostrar_menu(ANCHO)
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
        valor_busqueda = input('INGRESE EMAIL DEL ALUMNO A ACTUALIZAR :')
        posicion_busqueda = buscar_alumnos(valor_busqueda,lista_alumnos)
        if posicion_busqueda == -1:
            print("NO SE ENCONTRO EL ALUMNO SOLICITADO") 
        else:
            print(f'ALUMNO A ACTUALIZAR: {lista_alumnos[posicion_busqueda].get("nombre")}')
            nuevo_nombre = input("NOMBRE: ")
            nuevo_email = input("EMAIL: ")
            nuevo_celular = input("CELULAR: ")
            dic_actualizar_alumno = {
                'nombre':nuevo_nombre,
                'email':nuevo_email,
                'celular': nuevo_celular
            }
        lista_alumnos[posicion_busqueda] = dic_actualizar_alumno
        print("alumno actualizado")
    elif (opcion == 4):
        print("="*ANCHO)
        print(" "*10 + "[4] ELIMINAR ALUMNO")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE EMAIL DEL ALUMNO A ELIMINAR :')
        posicion_busqueda = -1
        posicion_busqueda = buscar_alumnos(valor_busqueda,lista_alumnos)
        if posicion_busqueda == -1:
            print("NO SE ENCONTRO EL ALUMNO SOLICITADO")
        else:
            lista_alumnos.pop(posicion_busqueda)
            print('ALUMNO ELIMINADO!!!')
    elif (opcion == 5):
        print("="*ANCHO)
        print(" "*10 + "[5] SALIR")
        print("="*ANCHO)
    else:
        print("="*ANCHO)
        print(" "*10 + "OPCION INVALIDA")
        print("="*ANCHO)
    time.sleep(1)