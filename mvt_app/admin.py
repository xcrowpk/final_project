from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
admin.site.register(Services)
admin.site.register(Clients)
admin.site.register(Staff)