capitales = {
    'Peru':'Lima',
    'Ecuador':'Quito',
    'Chile':'Santiago',
    'Colombia':'Bogota'
}
#recorrido por claves
for clave in capitales.keys():
    print(clave)
print('*'*50)
#recorrido por valores 
for value in capitales.values():
    print(value)
#recorrido por clave valor
for clave,valor in capitales.items():
    print(f'la capital de {clave} es {valor}')
#diccionary comprehension
paises = {valor:clave for clave,valor in capitales.items()}
print(paises)