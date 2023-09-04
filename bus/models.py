from django.db import models

# Create your models here.
DIAS = [(1,'Lunes'),(2,'Martes'),(3,'Miercoles'),(4,'Jueves'),(5,'Viernes'),(6,'Sabado')]
LUGAR = [(1,'Liebig a Colón'),(2,'Colón a Liebig')]



# class Time(models.Model):
#     hora = models.DateTimeField('Hora')

#     def __str__(self) -> str:
#         return self.hora.strftime("%H:%M")

# class BusSchedule(models.Model):
#     lugar = models.PositiveSmallIntegerField('Lugar', choices=LUGAR)
#     dia = models.PositiveSmallIntegerField('Dia',choices=DIAS)
#     hora = models.ForeignKey(Time,on_delete=models.CASCADE,null=models.SET_NULL)
    
#     class Meta:
#         verbose_name = "Bus"
#         verbose_name_plural = "Buses"

#     def __str__(self) -> str:
#         return self.get_lugar_display()

class Dia(models.Model):
    nombre = models.PositiveSmallIntegerField(choices=DIAS)  
    
    def __str__(self):
        return self.get_nombre_display()

class Horario(models.Model):
    hora = models.TimeField()

    def __str__(self):
        return str(self.hora.strftime("%H:%M"))

class HorarioPorDia(models.Model):
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE)
    horarios = models.ManyToManyField(Horario)

    def __str__(self):
        return f"{self.dia} - {', '.join([str(h) for h in self.horarios.all()])}"
    
class BusSchedule(models.Model):
    inicio = models.CharField(max_length=50)
    fin= models.CharField(max_length=50)
    HorarioDia = models.ManyToManyField(HorarioPorDia)

    def __str__(self) -> str:
        return f"{self.inicio} a {self.fin} - {','.join([str(d.dia) for d in self.HorarioDia.all()])}"