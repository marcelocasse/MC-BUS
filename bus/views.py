from django.shortcuts import render

from .models import Sector,Horario,Lugar,Localidad

from django.http.response import JsonResponse,HttpResponse

from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def mostrar_buses(request):
    buses = Sector.objects.all()
    context = {'data':buses}
    return render(request,'bus/html/index.html',context)

def index(request):
    return render (request,'bus/html/index.html',{})

def get_sector(request,sector):
    bus = Sector.objects.filter(nombre_sector=sector)
    context = {'data':bus}
    return render(request,'bus/html/index.html',context)

#-- API'S --#
def  update_horarios(request):
    listadehorarios = ['06:10', '07:00', '08:00', '10:20', '12:35', '15:25', '17:50', '19:50', '06:15', '07:05', '08:05', '10:25', '12:40', '15:30', '17:55', '19:55', '06:20', '07:10', '08:15', '10:30', '12:45', '15:35', '18:00', '20:00', '07:20', '08:25', '10:45', '13:05', '15:40', '18:20', '20:20', '07:30', '08:35', '10:55', '13:15', '15:50', '18:30', '20:30', '07:40', '08:40', '11:00', '13:20', '15:55', '18:35', '20:35', '06:40', '07:50', '08:55', '11:05', '13:30', '16:00', '18:45',
                   '20:45', '06:45', '08:00', '09:00', '11:45', '13:30', '16:30', '19:00', '20:45', '06:50', '08:05', '09:10', '11:50', '13:40', '16:35', '19:05', '06:55', '08:10', '09:15', '11:55', '13:50', '16:40', '19:10', '07:10', '08:20', '09:25', '12:05', '14:00', '16:50', '19:20', '07:30', '08:50', '09:55', '12:35', '14:30', '17:20', '19:45', '21:05', '07:35', '08:55', '10:00', '12:40', '14:35', '17:25', '19:50', '21:10', '07:40', '09:00', '10:05', '12:45', '14:40', '17:30', '19:55', '21:15']

    n = list(set(listadehorarios))

    n.sort()

    for i in n:
        hora = Horario(hora=i)
        hora.save()
    return JsonResponse({"Carga":"Completa"})

def api_sector(request):
    localidad = list(Localidad.objects.all())
    result = {"data" : []}

    for local in localidad:
            item = {}
            item['id'] = local.pk
            item['sector'] = local.nombre_localidad
            item['lugares'] = []
            
            sectores = list(Sector.objects.filter(nombre_sector=local.id))
            for sector in sectores:
                sub_item = {}
                sub_item['id'] = sector.lugar.pk
                sub_item['nombre_lugar'] = sector.lugar.nombre_lugar
                item['lugares'].append(sub_item)
            
            # horario_del_lugar = Horario.objects.filter(sector__id= sector.pk)
            # horario_formateado = []

            # for horario in horario_del_lugar:
            #     hora = horario.hora
            #     horario_formateado.append(hora)
                    
            # sub_item['horarios'] = horario_formateado

            result["data"].append(item)

            
    return JsonResponse(result,safe=False)

def api_sector_lugar(request,id_sector):
    try:
        localidades = Sector.objects.filter(nombre_sector_id=id_sector)
        
        item = {'lugares' : []}
        for local in localidades:
            sub_item = {}
            sub_item['id_lugar'] = local.lugar.pk
            sub_item['nombre_lugar'] = local.lugar.nombre_lugar
            item['lugares'].append(sub_item)
        return JsonResponse(data=item,safe=False)
    except ObjectDoesNotExist:
        return HttpResponse("No encontrado")



def api_lugar_horarios(request,id_sector):
    try:
        horario_del_lugar = Horario.objects.filter(sector__lugar_id= id_sector)
        lugar = Lugar.objects.get(id=id_sector)
        
        item = {}
        item['Id_Sector'] = id_sector
        item['Lugar'] = lugar.nombre_lugar
        
        horario_formateado = []

        for horario in horario_del_lugar:
            horario_formateado.append(horario.hora.strftime('%H:%M'))
        
        item['Horarios'] = horario_formateado

        return JsonResponse(data={'message': 'Success', 'data': item}, safe=False)
    except ObjectDoesNotExist:
        return JsonResponse(data={'message':"No encontrado"})
    

def api_lugar_final(request,id_lugar):
    try:
        localidades_final = Sector.objects.all().exclude(lugar=id_lugar)

        item = {'lugares' : []}
        for local in localidades_final:
            sub_item = {}
            sub_item['id_lugar'] = local.lugar.pk
            sub_item['nombre_lugar'] = local.lugar.nombre_lugar
            item['lugares'].append(sub_item)

        return JsonResponse(data={'message': 'Success', 'data': item}, safe=False)
    except ObjectDoesNotExist:
        return JsonResponse(data={'message':"No encontrado"})

