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