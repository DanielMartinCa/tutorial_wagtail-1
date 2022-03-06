'''
crear personal

ejecutar:

python manage.py shell < datos/crear_personal.py
'''

from personalempresa.models import PersonalEmpresa
from django.utils.text import slugify
import json
import os
'''
{"id":1,
"first_name":"Jens",
"last_name":"Blasli",
"email":"jblasli0@unc.edu",
"gender":"Female",
"department":"Marketing"
},

'''
#lista de personas del json
if os.path.exists("datos/PersonalEmpresa.json"):
    personal = json.load(open("datos/PersonalEmpresa.json", encoding="utf-8"))
else:
    personal = json.load(open("PersonalEmpresa.json", encoding="utf-8"))

for p1 in personal:
    p = PersonalEmpresa()
    p.id = p1["id"]
    p.nombre = p1["first_name"]
    p.apellidos = p1["last_name"]
    p.email = p1["email"]
    p.genero = p1["gender"]
    p.departamento = p1["department"]
    p.save()