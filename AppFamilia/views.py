from django.shortcuts import render
from django.http import HttpResponse
from AppFamilia.models import Fam

# Create your views here.

def fam(request):
    fam1 = Fam(nombre="Luis", edad="32", cumple="1990-08-02")
    fam1.save()
    fam2 = Fam(nombre="Daniela", edad="34", cumple="1988-05-26")
    fam2.save()
    fam3 = Fam(nombre="Diego", edad="34", cumple="1988-12-01")
    fam3.save()

    return HttpResponse(f"mis familiares son: {fam1.nombre}, tiene {fam1.edad} años y nacio el {fam1.cumple}. {fam2.nombre}, tiene {fam2.edad} años y nacio el {fam2.cumple}. {fam3.nombre}, tiene {fam3.edad} años y nacio el {fam3.cumple}.")