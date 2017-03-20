from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=140, null=False)
    password = models.CharField(max_length=50, null=False)
    username = models.CharField(max_length=15, null=False)
    aPaterno = models.CharField(max_length=140, null=False)
    aMaterno = models.CharField(max_length=140, null=False)
    fNacimiento = models.DateField(default = '', null=False)
    calle = models.CharField(max_length=50,default='', null=False)
    colonia = models.CharField(max_length=50,default='', null=False)
    cP = models.IntegerField()