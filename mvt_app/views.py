#importamos herramientas varias de django
from distutils.command.register import register
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from mvt_app.models import *
from mvt_app.forms import *

def index(request):

    return render(request, "mvt_app/index.html")

#SERVICES
def view_services(request):
    
    services_list = Services.objects.all()
    return render(request, "mvt_app/view_services.html", 
                  {'services_list':services_list})
    
#def add_services(request):   
  
#STAFF  
def view_staff(request):
    
    staff_list = Staff.objects.all()
    return render(request, "mvt_app/view_staff.html", 
                  {'staff_list':staff_list})   
    
def add_staff(request):
    
    if request.method == 'POST':
        staff_form = Staff(request.POST)
        print(staff_form)
        if staff_form.is_valid:   #Si pasó la validación de Django
            staff_info = staff_form.cleaned_data
            staffs = Staff(roll = staff_info['roll'],
                           name = staff_info['name'],
                           lastname = staff_info['lastname'])
            staffs.save()
            return render(request, "mvt_app/index.html") #Vuelvo al inicio o a donde quieran
    else:
        staff_form = Staff()
        return render(request, "mvt_app/add_staff.html", {"staff_form":staff_form})
        
     
#CLIENTS
def view_clients(request):
    
    clients_list = Clients.objects.all()
    return render(request, "mvt_app/view_clients.html", 
                  {'clients_list':clients_list}) 

def add_clients(request):
    
    if request.method == 'POST':
        clients_form = Register(request.POST)
        print(clients_form)
        if clients_form.is_valid:   #Si pasó la validación de Django
            info = clients_form.cleaned_data
            clients = Clients(user = info['user'],
                              name = info['name'],
                              lastname = info['lastname'],
                              email = info['email'])
            clients.save()
            return render(request, "mvt_app/index.html") #Vuelvo al inicio o a donde quieran
    else:
        clients_form = Register()
        return render(request, "mvt_app/add_clients.html", {"clients_form":clients_form})
    
#SEARCH
"""def search(request):

      if  request.GET["camada"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            camada = request.GET['camada'] 
            cursos = Curso.objects.filter(camada__icontains=camada)

            return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})

      else: 

	      respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)"""