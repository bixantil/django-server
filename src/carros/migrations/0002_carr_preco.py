# Generated by Django 2.0.7 on 2021-12-08 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carr',
            name='Preco',
            field=models.TextField(default='null'),
        ),
    ]