from django.shortcuts import render
from .models import Sector,Parada,Horario
from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,authentication_classes, permission_classes

def base(request):
    return render(request,'bus/html/bus.html',{})


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_sectores(request):
    try:
        result = {'data':[]}
        sector = list(Sector.objects.all())
        for sec in sector:
            item = {}
            item['id'] = sec.pk
            item['sector_nombre'] = sec.nombre_sector
            result['data'].append(item)
        
        return JsonResponse(result,safe=False)
    
    except ObjectDoesNotExist:
        return JsonResponse(data={'message':"No encontrado"})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_bus(request,id):
    try:
        result = []
        paradas = list(Parada.objects.filter(autobus_id=id))
        for parada in paradas:
            item = {}
            item['id'] = parada.pk
            item['nombre_parada'] = parada.nombre_parada
            result.append(item)
        return JsonResponse(result,safe=False)
    except ObjectDoesNotExist:
        return JsonResponse(data={'message':"No encontrado"})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
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
