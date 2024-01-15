from django.db import models

# Create your models here.

class Country(models.Model):
    namecountry = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return str(self.namecountry)
    
    
class Area(models.Model):
    namearea = models.CharField(max_length=100,blank=True, null=True)
    idcountry= models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return str(self.namearea)
    
    
class Subarea(models.Model):
    namesubarea = models.CharField(max_length=105)
    idarea = models.ForeignKey(Area, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.namesubarea)
    
class DocumentType(models.Model):
    nametype = models.CharField(max_length=50)
    def __str__(self):
        return str(self.nametype)
    
class Employee(models.Model):
    firstname = models.CharField(max_length=55)
    lastname = models.CharField(max_length=55)
    documentnumber = models.CharField(max_length=20)
    datehirirng = models.DateField()
    idsubarea = models.ForeignKey(Subarea, on_delete=models.CASCADE)
    iddocumenttype = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.firstname)