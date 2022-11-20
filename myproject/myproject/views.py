# aca van a estar todos los controladores
from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse("hola mundo")

def segunda_vista(request):
    return HttpResponse("ahora si")

def dia_de_hoy(request):
    diadehoy = datetime.datetime.now()
    cadena = f"hoy es{diadehoy}"
    return HttpResponse(cadena)

def probando_html(request):
    # se crean dos variables pára el diciconadio
    nom = "Cesar"
    ap  = "Pacheco"

    diccionario = {"nombre": nom, "apellido":ap, "edad": 32, "lista": [1,2,5,8,7,9,4,5,3,1,2] }

    archivo = open("D:/Users/acer/Desktop/coder1/myproject/templates/template.html")
    template = Template(archivo.read())
    archivo.close()
    contexto = Context(diccionario)

    documento = template.render(contexto)
    return HttpResponse(documento)