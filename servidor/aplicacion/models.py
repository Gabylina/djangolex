from django.db import models

# Create your models here.
SOL = [
    ("Familia", "Familia "),
    ("Civiles", "Civiles "),
    ("Laborales", "Laborales "),
    ("Penal antiguo", "Penal antiguo "),
    ("Por definir", "Por definir"),
]

class Cliente(models.Model):
    rut=models.CharField(max_length=12,primary_key=True)
    direccion=models.CharField(max_length=45, null=False)
    nombre=models.CharField(max_length=40, null=False)
    apellido=models.CharField(max_length=40,null=False)
    correo=models.CharField(max_length=200,null=False,unique=True)
    telefono=models.IntegerField(null=False)
    contraseña=models.CharField(max_length=12,null=False)
    
    def __str__(self):
        return f"{self.nombre}"

class Solicitud(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=50,null=False)
    tipo=models.CharField(choices=SOL,max_length=100,null=False)
    descripcion=models.CharField(max_length=500,null=False)

class Abogado(models.Model):
    rut=models.CharField(max_length=12,primary_key=True)
    nombre=models.CharField(max_length=40, null=False)
    
    def __str__(self):
        return f"{self.nombre}"

class Presupuesto(models.Model):
    id=models.AutoField(primary_key=True)
    Abogado=models.ForeignKey(Abogado,on_delete=models.PROTECT,null=False) 
    titulo_causa=models.CharField(max_length=50,null=False)
    horarios=models.IntegerField(null=False)
    tramites=models.IntegerField(null=False)
    total=models.IntegerField(null=False)

class Causa(models.Model):
    Abogado=models.ForeignKey(Abogado,on_delete=models.PROTECT,null=False) 
    titulo=models.CharField(max_length=50,null=False)
    
