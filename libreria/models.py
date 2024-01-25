from django.db import models

class tipoasociados(models.Model):
    id= models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=50)
 
    def __str__(self):
        fila = "" + self.Descripcion
        return fila

 
class asociados(models.Model):
    id= models.AutoField(primary_key=True)
    TipoDocument = models.ForeignKey(tipoasociados, on_delete=models.CASCADE)
    NoDocumento = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=100, verbose_name="Nombre")
    Direccion = models.CharField(max_length=100)
    Beneficiario = models.CharField(max_length=100)
    FechaIngreso = models.DateField(max_length=100)
    
    def __str__(self):
        fila = "Nombre: " + self.Nombre
        return fila   

class aportes(models.Model):
    id= models.AutoField(primary_key=True)
    idAsociado = models.ForeignKey(asociados, on_delete=models.CASCADE)
    ValorAporte = models.IntegerField()
    MesAporte = models.CharField(max_length=100, verbose_name="Mes")
    InteresAprote = models.IntegerField()
    DevolAporte = models.IntegerField()
    FechaAporte = models.DateField(max_length=100)
    AnoAporte = models.IntegerField()
    

    
    
    
    