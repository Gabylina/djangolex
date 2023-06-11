from django import forms
from .models import Cliente,Solicitud,Presupuesto





class formCrearCliente(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = '__all__'
        
class formSolicitud(forms.ModelForm):
    
    class Meta:
        model = Solicitud
        fields =  [ "titulo","tipo","descripcion"]
        
class formModiCLi(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre","apellido","direccion","correo","telefono","contraseña"]
        
class formPresuTec(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = ["Cliente","Abogado","titulo_causa","horarios","tramites","total"]
