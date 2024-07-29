import requests
import mysql.connector

def get_random_users(count=100):
    url = f'https://pokeapi.co/api/v2/pokemon/+{count}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print('error :',response.status_code)
        return []
    
def insert_users_to_mysql(users):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='db_codigo'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS tbl_pokemon(
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       nombre VARCHAR(255),
                       habilidades VARCHAR(255),
                       foto VARCHAR(255)
                       )
                       """)
        
        for usuario in users:
             nombre = usuario['name']
             habilidades = usuario['ability']
             foto = usuario['back_default']

             cursor.execute("""
                            INSERT INTO tbl_pokemon(nombre,habilidades,foto)
                            values(%s,%s,%s,%s)
                            """,(nombre,habilidades,foto))
             
             connection.commit()
        print('usuarios insertados exitosamente')

count_usuarios = int(input("inserte cantidad de usuarios a extraer : "))
usuarios = get_random_users(count_usuarios)
#print(usuarios)
insert_users_to_mysql(usuarios)