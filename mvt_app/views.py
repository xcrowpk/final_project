#importamos herramientas varias de django
from distutils.command.register import register
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

#importamos de distintos directorios el modelo "Family" y el fomulario "family_form"
from mvt_app.models import *
from mvt_app.forms import *

# Creamos una vista y con "HttpResponse" mostramos el argumento (la variable "name") en la pagina
def index(request):

    return render(request, "mvt_app/index.html")

def services(request):
    
    services_list = Services.objects.all()
    return render(request, "mvt_app/services.html", 
                  {'services_list':services_list})    
        
    
def add_clients(request):
    #return render(request, "mvt_app/family.html")
    if request.method == 'POST':
        form = Register(request.POST)
        print(form)
        if form.is_valid:   #Si pasó la validación de Django
            info = form.cleaned_data
            clients = Clients(user = info['user'],
                              name = info['name'],
                              lastname = info['lastname'],
                              email = info['email'])
            clients.save()
            return render(request, "mvt_app/index.html") #Vuelvo al inicio o a donde quieran
    else:
        form = Register()
        return render(request, "mvt_app/add_clients.html", {"form":form})
        
