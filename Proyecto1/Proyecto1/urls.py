"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from Proyecto1.views import saludo 
from Proyecto1.views import despedida 
from Proyecto1.views import dameFecha 
from Proyecto1.views import calculaEdad 
from Proyecto1.views import CursoC 
from Proyecto1.views import CursoCSS 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',saludo),
    path('despedida/',despedida),
    path('time/',dameFecha),
    path('cursoC/',CursoC),
    path('cursoCSS/',CursoCSS),
    path('edad/<int:edad>/<int:agno>',calculaEdad)
]
