"""ProyectoMecanico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from main import views as views_main
from backend import views as views_backend
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views_main.Index),
    path('infoCategorias/',views_main.InfoCategoria),
    path('galeriaMecanico/verImagen/<int:id>', views_main.verImagen),
    path('galeriaMecanico/', views_main.galeriaMecanico),
    path('subirImagen/', views_backend.SubirImagen),
    path('guardarImagen/', views_backend.GuardarImagen),  
    path('registro/', views_backend.registro),
    path('login/',views_backend.login),
    path('logout/',views_backend.logout),
    path('accounts/login/', views_backend.login),
    path('reinicio_contraseña/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reinicio_enviado/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reinicio/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reinicio_terminado/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('modificarImagen/<int:pk>', views_backend.ModificarImagen),
    path('eliminarImagen/<int:pk>', views_backend.EliminarImagen),
    path('accounts/', include('allauth.urls')),
    path('accounts/google/login/callback/index', views_main.Index),
    path('api/V1/', include('API.urls')),
]
