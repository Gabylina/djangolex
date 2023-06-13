from django.contrib import admin
from django.urls import path
from .views import index,iniciosesion,crearcuenta,solicitudes,PAGINAGABY,solicitudestecjuri,indextecjuri, presupuestostecjuri,pago



urlpatterns=[
    path('',index,name="index"),
    path('iniciosesion',iniciosesion,name="iniciosesion"),
    path('crearcuenta',crearcuenta,name="crearcuenta"),
    path('solicitudes',solicitudes,name="solicitudes"),
    path('PAGINAGABY',PAGINAGABY,name="PAGINAGABY"),
    path('solicitudestecjuri',solicitudestecjuri,name="solicitudestecjuri"),
    path('indextecjuri',indextecjuri,name="indextecjuri"),
    path('presupuestostecjuri',presupuestostecjuri,name="presupuestostecjuri"),
    path('pago/<int:pk>/',pago,name="pago"),
]