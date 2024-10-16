# Generated by Django 5.1.2 on 2024-10-14 23:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_balcao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Frutas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_fruta', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Dono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('balcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.balcao')),
                ('frutas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.frutas')),
            ],
        ),
    ]
