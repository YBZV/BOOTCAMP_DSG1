numeros = [1,2,3,4,5,6,7,8,9,10]
pares = []
print(numeros)
for numero in numeros:
    if(numero % 2 == 0):
        pares.append(numero)
print(pares)

#lis comprehensions
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)