from django.urls import path
from tienda.views import produccion_view

urlpatterns = [
    path('produccion/', produccion_view, name='produccion'),
]