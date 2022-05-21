from enum import unique
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class users(models.Model):
    nombre=models.CharField(verbose_name="Usuario",max_length=75,unique=True)
    dirreccion=models.TextField(verbose_name="Direccion de usuario",null=True)


    def __str__(self):
        return "{0} :: {1}".format(self.nombre , self.dirreccion)


    class Meta:
        verbose_name= "usuario"
        verbose_name_plural = "Usuarios"


class mascota(models.Model):
    nombre=models.CharField(verbose_name="Nombre mascota",max_length=30,unique=False)
    correo=models.EmailField(verbose_name="correo de contacto",max_length=50,null=False)
    fecha=models.DateField(verbose_name="fecha de naciomiento",auto_now=False,auto_now_add=False,null=False)

    def __str__(self):  
            return "{0} :: {1}".format(self.nombre,self.correo,self.fecha)

    class Meta:
        verbose_name="mascota"
        verbose_name_plural="mascotas"


class juguete(models.Model):
    tipo=models.CharField(verbose_name="tipo de juguete",max_length=20,unique=False)
    descripcion=models.TextField(verbose_name="Descripcion de juegute",null=False)
    compra=models.DateField(verbose_name="fecha de compra",auto_now_add=True,null=False)

    def __str__(self):
        return "Fecha de compra: {0}".format(self.compra)
        "Fecha de compra: {0}".format(self.compra),


    class meta:
        verbose_name="juguete"
        verbose_name_plurak="juegutes"