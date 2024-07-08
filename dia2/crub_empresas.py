import os
import tabulate
import time
from librerias.lib_empresas import mostrar_menu,buscar_empresa,cargar_datos,grabar_datos

f = open('empresas.txt','w')
f = open('empresas.txt','r')
str_empresa = f.read()
f.close()

lista_empresa = cargar_datos(str_empresa)

ANCHO = 50
opcion = 0
while(opcion < 5):
    os.system("clear")
    mostrar_menu(ANCHO)
    opcion = int(input("INGRESE LA OPCION : "))
    os.system("clear")
    if(opcion == 1):
        print("="*ANCHO)
        print(" "*10 + "[1] REGISTRAR EMPRESA")
        print("="*ANCHO)
        ruc = input("RUC: ")
        razonsocial = input("RAZON SOCIAL: ")
        direccion = input("DIRECCION: ")
        dic_nuevo_empresa = {
            'ruc':ruc,
            'razonsocial':razonsocial,
            'direccion':direccion
        }
        lista_empresa.append(dic_nuevo_empresa)
        print("EMPRESA REGISTRADA CON EXITO")
    elif (opcion == 2):
        print("="*ANCHO)
        print(" "*10 + "[2] MOSTRAR EMPRESA")
        print("="*ANCHO)
        cabeceras = ["RUC", "RAZON SOCIAL","DIRECCION"]
        tabla = [empresa.values() for empresa in lista_empresa]
        print(tabulate.tabulate(tabla,headers=cabeceras,tablefmt="grid"))
        input("presiona ENTER para continuar...")
    elif (opcion == 3):
        print("="*ANCHO)
        print(" "*10 + "[3] ACTUALIZAR EMPRESA")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE RAZON SOCIAL DEL EMPRESA A ACTUALIZAR :')
        posicion_busqueda = -1
        posicion_busqueda = buscar_empresa(valor_busqueda,lista_empresa)
        if posicion_busqueda == -1:
            print("NO SE ENCONTRO LA EMPRESA SOLICITADO") 
        else:
            print(f'EMPRESA ACTUALIZAR: {lista_empresa[posicion_busqueda].get("razonsocial")}')
            nuevo_ruc = input("RUC: ")
            nuevo_razonsocial = input("RAZON SOCIAL: ")
            nuevo_direccion = input("DIRECCION: ")
            dic_actualizar_empresa = {
                'ruc':nuevo_ruc,
                'razonsocial':nuevo_razonsocial,
                'direccion': nuevo_direccion
            }
        lista_empresa[posicion_busqueda] = dic_actualizar_empresa
        print("empresa actualizado")
    elif (opcion == 4):
        print("="*ANCHO)
        print(" "*10 + "[4] ELIMINAR EMPRESA")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE RAZON SOCIAL DE LA EMPRESA A ELIMINAR :')
        posicion_busqueda = buscar_empresa(valor_busqueda,lista_empresa)
        if posicion_busqueda == -1:
            print("NO SE ENCONTRO LA EMPRESA SOLICITADA")
        else:
            lista_empresa.pop(posicion_busqueda)
            print('EMPRESA ELIMINADO.')
    elif (opcion == 5):
        print("="*ANCHO)
        print(" "*10 + "[5] SALIR")
        str_empresa = grabar_datos(lista_empresa)
        fsalida = open('empresas.txt','w')
        fsalida.write(str_empresa)
        fsalida.close()
        print("="*ANCHO)
    else:
        print("="*ANCHO)
        print(" "*10 + "OPCION INVALIDA")
        print("="*ANCHO)
    time.sleep(1)