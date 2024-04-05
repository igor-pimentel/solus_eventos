from django.urls import path
from gerenciador_de_eventos.views import index

urlpatterns = [
    path('', index),
]