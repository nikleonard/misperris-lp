from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    run = forms.CharField(max_length=12)
    fechaNacimiento = forms.DateField()
    region = forms.CharField(max_length=50)
    comuna = forms.CharField(max_length=50)
    telefono = forms.CharField(max_length=9)
    TIPO_VIVIENDA = (
        ('CASAPATIOGRANDE','Casa con patio grande'),
        ('CASAPATIOPEQUEÑO','Casa con patio pequeño'),
        ('CASASINPATIO', 'Casa sin patio'),
        ('DEPARTAMENTO', 'Departamento')
    )
    tipoVivienda = forms.ChoiceField(choices=TIPO_VIVIENDA)

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'password1', 'password2','run','fechaNacimiento','region','comuna','telefono','tipoVivienda' )