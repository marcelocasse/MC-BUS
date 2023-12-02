from django.shortcuts import render

#from .models import Bus,Parada,Ruta

from .models import Sector,Autobus,Parada,Horario

from django.http.response import JsonResponse,HttpResponse

from django.core.exceptions import ObjectDoesNotExist


def base(request):
    return render(request,'bus/html/bus.html',{})


def api_sectores(request):
    result = {'data':[]}
    sector = list(Sector.objects.all())
    for sec in sector:
        item = {}
        item['id'] = sec.pk
        item['sector_nombre'] = sec.nombre_sector
        result['data'].append(item)

    return JsonResponse(result,safe=False)
    
def api_bus(request,id):
    result = []
    paradas = list(Parada.objects.filter(autobus_id=id))
    for parada in paradas:
        item = {}
        item['id'] = parada.pk
        item['nombre_parada'] = parada.nombre_parada
        result.append(item)
    return JsonResponse(result,safe=False)

def api_parada_horarios(request,id):
    try:
        horarios = list(Horario.objects.filter(parada_id=id))
        parada = Parada.objects.get(pk=id)

        item = {}
        item['parada'] = parada.nombre_parada
        
        horario_formateado = []
        for horario in horarios:

            horario_formateado.append(horario.hora.strftime('%H:%M'))
        item['horarios'] = horario_formateado
        return JsonResponse(data={'data':item})
    
    except ObjectDoesNotExist:
        return JsonResponse(data={'message':"No encontrado"})

# item['autobuses'] = []
        # autobus = list(Autobus.objects.filter(sector_id=sec.pk))
        # for auto in autobus:
        #     sub_item = {}
        #     sub_item['id'] = auto.pk
        #     sub_item['chofer'] = auto.chofer
        #     sub_item['placa'] = auto.placa
        #     sub_item['capacidad'] = auto.capacidad
        #     sub_item['paradas'] = []
        #     paradas = list(Parada.objects.filter(autobus_id=auto.pk))
        #     for parada in paradas:
        #         sub_item['paradas'].append(parada.nombre_parada)
        #     item['autobuses'].append(sub_item) 




# Create your views here.
# def mostrar_buses(request):
#     buses = Sector.objects.all()
#     context = {'data':buses}
#     return render(request,'bus/html/index.html',context)

# def index(request):
#     return render (request,'bus/html/index.html',{})

# def get_sector(request,sector):
#     bus = Sector.objects.filter(nombre_sector=sector)
#     context = {'data':bus}
#     return render(request,'bus/html/index.html',context)

#-- API'S --#

# def api_buses(request):
#     result = {"data" : []}

#     if Bus.objects.exists():

#         buses = list(Bus.objects.all())

#         for bus in buses:
#                 item = {}
#                 item['id'] = bus.pk
#                 item['bus_nombre'] = bus.nombre_bus
#                 item['paradas'] = []
                
#                 rutas = list(Ruta.objects.filter(bus=bus.id))
#                 for ruta in rutas:
#                     sub_item = {}
#                     sub_item['id'] = ruta.parada.pk
#                     sub_item['nombre_parada'] = ruta.parada.nombre_parada
#                     item['paradas'].append(sub_item)

#                 result["data"].append(item)
#         return JsonResponse(result,safe=False)
#     else:
#         result["data"].append("Not Found")
#         return JsonResponse(result,safe=False)

# def api_bus_paradas(request,id_bus):
#     try:
#         rutas = Parada.objects.filter(ruta__bus_id=id_bus).distinct()
        
#         item = {'paradas' : []}
#         for ruta in rutas:
#             sub_item = {}
#             sub_item['id'] = ruta.pk
#             sub_item['nombre_parada'] = ruta.nombre_parada
#             item['paradas'].append(sub_item)
#         return JsonResponse(data=item,safe=False)
#     except ObjectDoesNotExist:
#         return HttpResponse("No encontrado")



# def api_parada_horarios(request,id_bus,id_parada):
#     try:
#         parada_horarios = list(Ruta.objects.filter(bus__pk=id_bus,parada__pk=id_parada))
#         parada = Parada.objects.get(pk=id_parada)

#         item = {}
#         item['parada'] = parada.nombre_parada
#         horario_formateado = []

#         for horario in parada_horarios:
#             horario_formateado.append(horario.hora_llegada.strftime('%H:%M'))
        
#         item['horarios'] = horario_formateado

#         return JsonResponse(data={'message': 'Success', 'data': item}, safe=False)
#     except ObjectDoesNotExist:
#         return JsonResponse(data={'message':"No encontrado"})
    

# def api_parada_final(request,id_bus,id_parada):
#     try:
#         paradas_finales = Parada.objects.filter(ruta__bus_id=id_bus).exclude(pk=id_parada).distinct()

#         item = {'paradas' : []}
#         for parada in paradas_finales:
#             sub_item = {}
#             sub_item['id'] = parada.pk
#             sub_item['nombre_parada'] = parada.nombre_parada
#             item['paradas'].append(sub_item)

#         return JsonResponse(data={'message': 'Success', 'data': item}, safe=False)
#     except ObjectDoesNotExist:
#         return JsonResponse(data={'message':"No encontrado"})

