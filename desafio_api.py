# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-04-01
# RLAB-23-02-09-0044-2
#

# Librerias
import requests
import json

# Variables
url = "https://reqres.in/api/users"

# Obtenga toda la información de los usuarios retornada por la API, guárdela en una
# variable llamada users_data e imprímala en pantalla.(3 Puntos)
request = requests.request("GET", url, headers={}, data={})
users_data = json.loads(request.text)
print(users_data)
print(request)

# 2. Cree un usuario que tenga de nombre Ignacio y de trabajo Profesor. Guarde el
# diccionario de respuesta en una variable llamada created_user e imprímala en
# pantalla. (2 Puntos)
data_ignacio = {"6": {"id": 7, "first_name": "Ignacio", "work": "Profesor"}}
created_user = requests.post(url, json=data_ignacio)
print(created_user.text)
print(created_user)

# 3. Actualice un usuario llamado morpheus para que tenga un campo llamado residence
# igual a zion. Guarde el diccionario de respuesta en una variable llamada
# updated_user e imprímala en pantalla. (3 Puntos)
url_put = "https://reqres.in/api/users/1"
data_morpheus = {"first_name": "morpheus", "residence": "zion"}
updated_user = requests.put(url_put, data_morpheus)
print(updated_user.text)
print(updated_user)

# 4. Elimine un usuario llamado Tracey. Imprima el código de respuesta en pantalla.
# (2 Puntos)
Tracey = requests.delete("https://reqres.in/api/users/6")
print(Tracey)