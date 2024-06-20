from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('error/', views.error, name='error'),
    path('inicio_sesion/', views.iniciar_sesion, name='inicio_sesion'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),

]
