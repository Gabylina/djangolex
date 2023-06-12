from django.contrib import admin
from django.urls import path
from .views import index,iniciosesion,crearcuenta,solicitudes,pago



urlpatterns=[
    path('',index,name="index"),
    path('iniciosesion',iniciosesion,name="iniciosesion"),
    path('crearcuenta',crearcuenta,name="crearcuenta"),
    path('solicitudes',solicitudes,name="solicitudes"),
    path('pago',pago,name="pago"),
]