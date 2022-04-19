from django.db import models

"""
Definimos la estructura de los campos en la base de datos q vamos a crear luego con el comando
"python manage.py makemigrations"
"""

class Services (models.Model):
    
    services = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.services}"

    
class Clients (models.Model):
    
    user = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
    def __str__(self):
        return f"User: {self.user} - Name: {self.name} - Lastname: {self.lastname} - E-Mail {self.email}"
