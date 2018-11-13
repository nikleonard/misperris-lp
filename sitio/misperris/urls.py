from django.urls import path,include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('iniciarSesion.html', views.iniciarSesion, name='iniciarSesion'),
    path('registro.html', views.registro, name='registro'),
    #path('signup.html', views.signup, name='signup'),
    path('cuentas/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
        '/img/', document_root=settings.STATIC_ROOT+'/misperris/img')
