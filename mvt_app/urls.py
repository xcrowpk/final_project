#importamos "herramientas" de django
from django.urls import path, include
#importamos la carpeta "views" del proyecto
from mvt_app import views

#aca definimos la direccion URL por la cual accedemos a la vista que armamos, desde el navegador.
urlpatterns = [
    path('', views.index, name = 'index'),
    path('add_clients/', views.add_clients, name = 'add_clients'),
    path('view_services/', views.view_services, name = 'view_services'),
    path('staff/', views.view_staff, name = 'view_staff'),
    path('add_staff/', views.add_staff, name = 'add_staff'),
    path('view_clients/', views.view_clients, name = 'view_clients'),
    path('search_staff/', views.search_staff, name = 'search_staff'),
    path('search_result/', views.search_result, name = 'search_result'),
    path('about_us/', views.about_us, name = 'about_us'),
]