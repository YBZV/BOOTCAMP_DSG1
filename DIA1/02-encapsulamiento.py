class usuario:
    email = 'yessizegarrav@hotmail.com'
    password = 'qwerty123'

    def __init__(self):
        pass
    def login(self,email,password):
        if(self.email == email and self.password == password):
            print (f"Bienvenido {self.email}")
        else:
            print('datos incorrectos')
print('LOGIN DE USUARIOS')
email = input('ingrese email: ')
password = input('Ingrese Password: ')
usuario = usuario()
usuario.login(email,password)