from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Rescatado)
admin.site.register(models.Perfil)