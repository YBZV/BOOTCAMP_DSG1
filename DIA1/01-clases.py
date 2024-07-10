class Automovil:
    #atributos
    def __init__(self,aa,pl,col,mar):
        self.anio = aa
        self.placa = pl
        self.color = col
        self.marca = mar
    def encender(self):
        print ('encender ' + self.marca)   
#objetos
vw = Automovil(1970,'ch-2314','amarillo','volkswagen')
vw.encender()

tico = Automovil(1990,'ah-2562','rojo','daewo')
tico.encender()

