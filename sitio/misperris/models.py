from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Rescatado(models.Model):
        nombre=models.CharField(max_length=50)
        ESTADOS = (
            ('RESCATADO','Rescatado'),
            ('DISPONIBLE','Disponible'),
            ('ADOPTADO','Adoptado')
        )
        estado=models.CharField(max_length=10,choices=ESTADOS)
        razaPredominante=models.CharField(max_length=50)
        descripcion=models.CharField(max_length=255)
        foto=models.ImageField(upload_to='rescatados')

# Perfil de usuario extendido
class Perfil(models.Model):
    # Para evitar warning.
    objects = models.Manager() 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    run = models.CharField(max_length=12)
    fechaNacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    region = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    TIPO_VIVIENDA = (
        ('CASAPATIOGRANDE','Casa con patio grande'),
        ('CASAPATIOPEQUEÑO','Casa con patio pequeño'),
        ('CASASINPATIO', 'Casa sin patio'),
        ('DEPARTAMENTO', 'Departamento')
    )
    tipoVivienda = models.CharField(max_length=20,choices=TIPO_VIVIENDA,verbose_name="Tipo de Vivienda")

"""
@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    instance.Perfil.save()
    """