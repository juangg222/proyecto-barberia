"""
URL configuration for barberia project.

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
from barberia_app import views  # Asegúrate de que "barberia_app" sea el nombre correcto de tu aplicación

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel de administración
    path('', views.home, name='home'),  # Página principal
    path('servicios/', views.servicios, name='servicios'),  # Página de servicios
    path('agenda/', views.agenda, name='agenda'),  # Página de agenda
    path('confirmacion/', views.confirmacion, name='confirmacion'),  # URL para la confirmación
]
