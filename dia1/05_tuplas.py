dias =  ("lunes", "martes", "miercoles" ,"jueves")
print(dias)
#tuplas no se puede cambiar o eliminar pero se puede convertir en lista y despues la cambio a tuple
dias = list(dias)
print(type(dias))
dias.append("viernes")
dias =tuple(dias)
print(type(dias))
for dia in dias:
    print(dia)
