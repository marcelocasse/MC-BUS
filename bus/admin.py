from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Sector)
admin.site.register(Autobus)
admin.site.register(Parada)

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('hora','parada_id','parada')

