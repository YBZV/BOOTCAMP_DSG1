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
def buscar_alumnos(valor_busqueda,lista_alumnos):
    posicion_busqueda = -1
    for posicion in range(len(lista_alumnos)):
            dic_alumno = lista_alumnos[posicion]
            if valor_busqueda in dic_alumno.values():
               posicion_busqueda = posicion
               break
    return posicion_busqueda