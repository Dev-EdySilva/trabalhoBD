# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-05 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id_funcionario', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('rg', models.CharField(max_length=25)),
            ],
        ),
    ]
