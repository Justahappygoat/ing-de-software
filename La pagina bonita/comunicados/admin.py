from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Comunicado
from .models import Categoria


admin.site.register(Comunicado)
admin.site.register(Categoria)