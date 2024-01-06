from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    #-- Routes --#
    path('',views.base),

    #-- API --#
    path('api/sectores',views.api_sectores),
    path('api/bus/<int:id>',views.api_bus),
    path('api/parada/<int:id>/horarios',views.api_parada_horarios),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)