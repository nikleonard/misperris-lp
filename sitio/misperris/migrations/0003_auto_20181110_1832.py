# Generated by Django 2.0.9 on 2018-11-10 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misperris', '0002_auto_20181110_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rescatado',
            name='foto',
            field=models.ImageField(upload_to='rescatados'),
        ),
    ]
