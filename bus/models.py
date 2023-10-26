from django.db import models

# Create your models here.

class Horario(models.Model):
    hora = models.TimeField(unique=True)


    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self) -> str:
        return self.hora.strftime('%H:%M')
    

class Lugar(models.Model):
    nombre_lugar = models.CharField(max_length=50,null=False,blank=False)

    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'

    def __str__(self) -> str:
        return self.nombre_lugar

class Localidad(models.Model):
    nombre_localidad = models.CharField(max_length=50,null=False,blank=False)

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'

    def __str__(self) -> str:
        return self.nombre_localidad
    

class Sector(models.Model):
    nombre_sector = models.ForeignKey("Localidad",on_delete=models.CASCADE,null=False)
    lugar = models.ForeignKey("Lugar",on_delete=models.CASCADE,null=False,)
    horarios = models.ManyToManyField("Horario")

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'

    def __str__(self) -> str:
        return f"{self.nombre_sector} | {self.lugar}"