from django.template import Template, Context, loader
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola!")

def fami(request):

    mama = "Graciela"

    edad = "63"

    diccionario = {"name":mama, "ages":edad}

    plantilla = loader.get_template("plantillas.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)