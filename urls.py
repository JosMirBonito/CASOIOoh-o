from django.urls import path
from tienda.views import produccion_view

urlpatterns = [
    path('', produccion_view, name='home'),
    path('produccion/', produccion_view, name='produccion'),
]