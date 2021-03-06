#importamos "forms" de django
from django import forms

#Creamos el formulario q vamos a llenar cuando accedemos a "family.html" desde el navegador
class Clients_form(forms.Form):
    
    user = forms.CharField(max_length=50)
    name = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    
class Staff_form(forms.Form):
    
    roll = forms.CharField(max_length=50)
    name = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)