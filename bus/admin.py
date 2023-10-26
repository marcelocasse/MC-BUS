from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    ordering = ('hora',)


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    ordering = ('nombre_lugar',)

@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    ordering = ('id',)

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('nombre_sector', 'lugar')
    search_fields = ('nombre_sector',)