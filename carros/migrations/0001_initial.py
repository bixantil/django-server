# Generated by Django 2.0.7 on 2021-12-08 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marca', models.TextField(default='null')),
                ('Modelo', models.TextField(default='null')),
                ('Motor', models.TextField(default='null')),
                ('Ano', models.TextField(default='null')),
                ('Cambio', models.TextField(default='null')),
                ('Combustivel', models.TextField(default='null')),
                ('Km', models.TextField(default='null')),
            ],
        ),
    ]