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
    nombre_lugar = models.CharField(max_length=20,null=False,blank=False)

    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'

    def __str__(self) -> str:
        return self.nombre_lugar
    
class Sector(models.Model):
    nombre_sector = models.CharField(max_length=20,null=False,blank=False)
    lugar = models.ForeignKey(Lugar,on_delete=models.CASCADE,related_name='lugar')
    horarios = models.ManyToManyField(Horario,related_name='horarios')

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'

    def __str__(self) -> str:
        return f"{self.nombre_sector} | {self.lugar}"