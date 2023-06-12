from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente, Solicitud, Presupuesto, Causa
from .forms import formCrearCliente, formSolicitud,formModiCLi,formSolicitud_Tec
# Create your views here.


def index(request):
    return render(request,'aplicacion/index.html')



def iniciosesion(request):
    
    
    
    
    return render(request,'aplicacion/Inicio_sesion.html')



def crearcuenta(request):
    
    form=formCrearCliente(request.POST or None)

    contexto={
        "form":form,
        
    }

    if form.is_valid():
        crearcli=form.save(commit=False)
        crearcli.save()
        return redirect(to="iniciosesion")
    
    return render(request,'aplicacion/CrearCuenta.html',contexto)


def pago(request):# para ir a pestaña de pago
    
    return render(request,'aplicacion/pago.html')


def solicitudes(request):
    people=Cliente.objects.all()
    solis=Solicitud.objects.all()
    pres=Presupuesto.objects.all()
    causa=Causa.objects.all()
    
    
    form=formSolicitud(request.POST or None)
    
    Cli=get_object_or_404(Cliente,rut='20.994.291-7')
    
    form_modi=formModiCLi(instance=Cli)
    
    contexto={
        "Cli":Cli,
        "personas":people,
        "form":form,
        "form_modi":form_modi,
        "solicitudes":solis,
        "presupuesto":pres,
        "causa":causa,
    }
    if request.method=="POST":
        form_modi=formModiCLi(data=request.POST,instance=Cli)
    
    if form.is_valid():
        newsoli=form.save(commit=False)
        datos=form.cleaned_data   
        newsoli.save()
        return redirect(to="solicitudes")
    
    if form_modi.is_valid():
        modcli=Cliente.objects.get(rut=Cli.rut)
        datos=form_modi.cleaned_data
        modcli.nombre=datos.get("nombre")
        modcli.apellido=datos.get("apellido")
        modcli.direccion=datos.get("direccion")
        modcli.correo=datos.get("correo")
        modcli.telefono=datos.get("telefono")
        modcli.contraseña=datos.get("contraseña")
        modcli.save()
        return redirect(to="solicitudes")
        
    return render(request,'aplicacion/Solicitudes.html',contexto)

def PAGINAGABY(request):
    
    return render(request,'aplicacion/PAGINAGABY.html')

def solicitudestecjuri(request):
    
    solic=Solicitud.objects.all()
    
    form=formSolicitud_Tec(request.POST or None)
    
    contexto={
        "form":form,
        "solicitudes":solic,
    }
        
    return render(request,'aplicacion/Tec_Juridico/Solicitudes_tec_juri.html',contexto)


def indextecjuri(request):
        
    return render(request,'aplicacion/Tec_Juridico/index_tec_juri.html')

def presupuestostecjuri(request):

    form = formPresuTec()

    if request.method == "POST":
        form = formPresuTec(request.POST)
    
    return render(request,'aplicacion/Tec_Juridico/presupuestos_tec_juri.html', { 'form' : form })
