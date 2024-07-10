class Persona:
   def __init__(self,nom,ema,):
    self.nombre = nom
    self.email = ema
   def mostrar(self):
    print("="*25)
    print(f"NOMBRE: {self.nombre}")
    print(f"EMAIL: {self.email}") 
class alumnos(Persona):
 def __init__(self,nom,ema,nota):
    super().__init__(nom,ema)
    self.nota = nota
    
class profesor(Persona):
   def __init__(self,nom,ema,esp):
      super().__init__(nom,ema)
      self.especialidad = esp
         

alumno1 = alumnos('yessica','YES@HOYMA',20)
alumno1.mostrar()
print(f"NOTA: {alumno1.nota}")

profesor1 = profesor('cesar','cesar@hotmail','base de datos')
profesor1.mostrar()
print(f"ESPECIALIDAD: {profesor1.especialidad}")