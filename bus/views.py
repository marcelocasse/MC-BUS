from django.shortcuts import render
from .models import HorarioPorDia,Horario,Dia #BusSchedule
from django.http.response import JsonResponse

# Create your views here.
def newbus(request):
    horario = HorarioPorDia.objects.all()
    # lugares = ["Liebig a Colón","Colón a Liebig"]
    ctx = {'horarios_por_dia':horario}
    return render(request,"bus/html/base.html",ctx)


def get_horarios(request):
    dia = list(HorarioPorDia.objects.filter(dia_id=1))
    horario  = [n.hora.strftime("%H:%M") for n in dia[0].horarios.all()]

    x = HorarioPorDia(dia=2)
    x.horarios.select_related()
    return JsonResponse({"Horarios":horario})

def get_dias(request):
    dias = list(Dia.objects.values())
    data = {"dias":dias}
    return JsonResponse(data)

def  update_horarios(request):
    listadehorarios = ['06:10', '07:00', '08:00', '10:20', '12:35', '15:25', '17:50', '19:50', '06:15', '07:05', '08:05', '10:25', '12:40', '15:30', '17:55', '19:55', '06:20', '07:10', '08:15', '10:30', '12:45', '15:35', '18:00', '20:00', '07:20', '08:25', '10:45', '13:05', '15:40', '18:20', '20:20', '07:30', '08:35', '10:55', '13:15', '15:50', '18:30', '20:30', '07:40', '08:40', '11:00', '13:20', '15:55', '18:35', '20:35', '06:40', '07:50', '08:55', '11:05', '13:30', '16:00', '18:45',
                   '20:45', '06:45', '08:00', '09:00', '11:45', '13:30', '16:30', '19:00', '20:45', '06:50', '08:05', '09:10', '11:50', '13:40', '16:35', '19:05', '06:55', '08:10', '09:15', '11:55', '13:50', '16:40', '19:10', '07:10', '08:20', '09:25', '12:05', '14:00', '16:50', '19:20', '07:30', '08:50', '09:55', '12:35', '14:30', '17:20', '19:45', '21:05', '07:35', '08:55', '10:00', '12:40', '14:35', '17:25', '19:50', '21:10', '07:40', '09:00', '10:05', '12:45', '14:40', '17:30', '19:55', '21:15']

    n = list(set(listadehorarios))

    n.sort()

    for i in n:
        hora = Horario(hora=i)
        hora.save()
    return JsonResponse({"Carga":"Completa"})

def update_horariopordia(request):

    diax = Dia.objects.values()
    print(diax.get_nombre_display)


def prueba(request):
    pass

    #1 - Obtenemos el id del dia
    #    dia = Dia.objects.get(id=1) //id=1 es lunes
    #2 - Creamos un nuevo objecto de HorarioPorDia
    #    hora = HorarioPorDia.objects.create(dia=dia)
    #3 - Obtenemos el id de varios horarios
    #    hour = Horario.objects.get(id=243)
    #4 - Agregamos al objecto creado la hora
    #    hora.horarios.add(hour)
    #5 - Guardamos
    #    hora.save()
    
    #    obtener los id del objecto ya creado en este caso lunes
    #    horas = HorarioPorDia.objects.first().horarios.values()
    #    x = [horas[n]['id'] for n in range(len(horas))]