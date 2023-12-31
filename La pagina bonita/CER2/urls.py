"""
URL configuration for CER2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from comunicados import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

admin.site.login = login_required(admin.site.login)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('registrar_comunicado/', views.registrar_comunicado, name='registrar_comunicado'),
    path('login/', auth_views.LoginView.as_view(template_name='comunicados/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


