# Generated by Django 2.0.9 on 2018-11-12 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misperris', '0005_auto_20181111_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='user',
        ),
    ]
