# Generated by Django 4.1.2 on 2022-10-16 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(null=True, upload_to='media/', verbose_name='Imagen'),
        ),
    ]
