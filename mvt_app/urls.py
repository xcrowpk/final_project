#importamos "herramientas" de django
from django.urls import path
#importamos la carpeta "views" del proyecto
from mvt_app import views

#aca definimos la direccion URL por la cual accedemos a la vista que armamos, desde el navegador.
urlpatterns = [
    path('', views.index),
    path('add_clients/', views.add_clients),
    path('view_services/', views.view_services),
    path('staff/', views.view_staff),
    path('add_staff/', views.add_staff),
    path('view_clients/', views.view_clients),
]
