def mostrar_menu(ancho):
    print("="*ancho)
    print(" " * 10 + "CRUD DE EMPRESAS")
    print("="*ancho)
    print("""
          [1] REGISTRAR EMPRESA
          [2] MOSTRAR EMPRESA
          [3] ACTUALIZAR EMPRESA
          [4] ELIMINAR EMPRESA
          [5] SALIR
    """)
    print("="*ancho)
    
def buscar_empresa(valor_buscado,lista_empresa):
    posicion_busqueda = -1
    for posicion in range(len(lista_empresa)):
        dic_empresa = lista_empresa[posicion]
        if valor_buscado in dic_empresa.values():
            posicion_busqueda = posicion
            break
    return posicion_busqueda
def cargar_datos(str_datos):
    lista_empresa = []
    lista_general = str_datos.splitlines()
    for str_registro in lista_general:
        lista_registro =str_registro.split(',')
        dic_registro = {
            'ruc': lista_registro[0],
            'razonsocial': lista_registro[1],
            'direccion': lista_registro[2],
        }
        lista_empresa.append(dic_registro)
    return lista_empresa
    
def grabar_datos(lista_empresa):
    str_empresa = ""
    for dic_registro in lista_empresa:
        for clave,valor in dic_registro.items():
            str_empresa += valor
            if clave != 'direccion':
                str_empresa += ','
            else:
                str_empresa += '\n'
    return str_empresa
    