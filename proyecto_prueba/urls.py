"""
URL configuration for proyecto_prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from prueba import views

urlpatterns = [
    path("admin/", admin.site.urls),
#    path("saludo/", views.saludo, name = "saludo"),
#    path("info/<str:nom>/<int:edad>/", views.info_usuario, name="informacion"),
#    path("saludo-nuevo/", views.nuevo_saludo, name="saludo-nuevo"),
#    path("suma/<int:num1>/<int:num2>/<str:ope>/", views.suma, name="suma"),
#    path("datos/", views.datos, name="datos"),
    path('', include('appVentas.urls') ),

]
