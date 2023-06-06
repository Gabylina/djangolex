from django.contrib import admin
from .models import Cliente, Solicitud,Abogado,Presupuesto,Causa

# Register your models here.

class admCliente(admin.ModelAdmin):
    list_display=["rut","direccion","nombre","apellido","correo","telefono","contraseña"]
    list_editable=[]
    
    class meta:
        model=Cliente

class admSolicitud(admin.ModelAdmin):
    list_display=["id","titulo","tipo","descripcion"]
    list_editable=[]
    
    class meta:
        model=Solicitud
    
class admAbogado(admin.ModelAdmin):
    list_display= ["rut","nombre"]
    list_editable= ["nombre"]
    
    class meta:
        model=Abogado
    
class admPresupuest(admin.ModelAdmin):
    list_display= ["id","Abogado","titulo_causa","horarios","tramites","total"]
    list_editable= ["titulo_causa","horarios","tramites","total"]
    
    class meta:
        model:Presupuesto
    
class admCausa(admin.ModelAdmin):
    list_display = ["Abogado","titulo"]
    list_editable = ["titulo"]
    
    class meta:
        model:Causa


admin.site.register(Cliente,admCliente)
admin.site.register(Solicitud,admSolicitud)
admin.site.register(Abogado,admAbogado)
admin.site.register(Presupuesto,admPresupuest)
admin.site.register(Causa,admCausa)

