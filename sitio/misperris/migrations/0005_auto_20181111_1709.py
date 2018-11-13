# Generated by Django 2.0.9 on 2018-11-11 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('misperris', '0004_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(max_length=12)),
                ('fechaNacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('region', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=9)),
                ('tipoVivienda', models.CharField(choices=[('CASAPATIOGRANDE', 'Casa con patio grande'), ('CASAPATIOPEQUEÑO', 'Casa con patio pequeño'), ('CASASINPATIO', 'Casa sin patio'), ('DEPARTAMENTO', 'Departamento')], max_length=20, verbose_name='Tipo de Vivienda')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterField(
            model_name='rescatado',
            name='estado',
            field=models.CharField(choices=[('RESCATADO', 'Rescatado'), ('DISPONIBLE', 'Disponible'), ('ADOPTADO', 'Adoptado')], max_length=10),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]