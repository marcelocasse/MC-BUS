from django.db import models

# Create your models here.


class Sector(models.Model):
    nombre_sector = models.CharField(max_length=50,null=False)
    ubicacion = models.CharField(max_length=50,null=False)
    
    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'

    def __str__(self) -> str:
        return self.nombre_sector

class Autobus(models.Model):
    chofer = models.CharField(max_length=50,null=False)
    placa = models.CharField(max_length=50,null=False)
    capacidad = models.PositiveSmallIntegerField()
    sector = models.ForeignKey(Sector,on_delete=models.CASCADE,null=False,blank=False,default="")

    class Meta:
        verbose_name = 'Autobus'
        verbose_name_plural = 'Autobuses'

    def __str__(self) -> str:
        return f"{self.chofer} | {self.placa} | {self.sector.nombre_sector}"


class Parada(models.Model):
    nombre_parada = models.CharField(max_length=50,null=False)
    autobus = models.ForeignKey(Autobus,on_delete=models.CASCADE,null=False,default="")

    class Meta:
        verbose_name = 'Parada'
        verbose_name_plural = 'Paradas'

    def __str__(self) -> str:
        return f"{self.nombre_parada}"
    
class Horario(models.Model):
    hora = models.TimeField(unique=True,null=False)
    parada = models.ForeignKey(Parada,on_delete=models.CASCADE,null=False,default="")

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self) -> str:
        return f"{self.hora.strftime('%H:%M')}"

# class Parada(models.Model):
#     nombre_parada = models.CharField(max_length=50,null=False,blank=False)

#     class Meta:
#         verbose_name = 'Parada'
#         verbose_name_plural = 'Paradas'

#     def __str__(self) -> str:
#         return self.nombre_parada

# class Bus(models.Model):
#     nombre_bus = models.CharField(max_length=50,null=False,blank=False)

#     class Meta:
#         verbose_name = 'Bus'
#         verbose_name_plural = 'Buses'

#     def __str__(self) -> str:
#         return self.nombre_bus
   

# class Ruta(models.Model):
#     bus = models.ForeignKey(Bus,on_delete=models.CASCADE,null=False)
#     hora_llegada = models.TimeField(null=False)
#     hora_salida = models.TimeField(null=False)
#     parada = models.ForeignKey(Parada,on_delete=models.CASCADE,null=False)

#     class Meta:
#         verbose_name = 'Ruta'
#         verbose_name_plural = 'Rutas'

#     def __str__(self) -> str:
#         return f"{self.bus_id} | {self.parada}"