from django.contrib import admin
from .models import Horario,Lugar,Sector

# Register your models here.

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    ordering = ('hora',)


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    ordering = ('nombre_lugar',)


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('nombre_sector', 'lugar')
    search_fields = ('nombre_sector',)