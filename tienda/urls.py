from django.urls import path
from .views import produccion_view

urlpatterns = [
    path('', produccion_view, name='produccion'),
]