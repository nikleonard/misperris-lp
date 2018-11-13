from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from misperris.models import Perfil
from django.contrib.auth.models import User
from django.utils.dateparse import parse_date


# Create your views here.
def index(request):
    return render(request,'misperris/index.html')
def iniciarSesion(request):
    return render(request,'misperris/iniciarSesion.html')


def registro(request):
    if request.method == 'POST':
        print(request.POST)
        user = User.objects.create_user(
            request.POST['usuario'],
            email=request.POST['email'],
            password=request.POST['clave'],
            first_name=request.POST['nombres'],
            last_name=request.POST['apellidos'])
        user.save()
        perfil = Perfil.objects.create(
            user=user,
            run=request.POST['run'],
            fechaNacimiento=parse_date(request.POST['fecnac']),
            region=request.POST['region'],
            comuna=request.POST['comuna'],
            telefono=request.POST['telefono'],
            tipoVivienda=request.POST['vivienda'])
        perfil.save()
    return render(request,'misperris/registro.html')

"""
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'misperris/signup.html', {'form': form})"""
