# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-27 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RHIN', '0010_funcionario_rg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ferias',
            name='end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='ferias',
            name='start',
            field=models.DateField(),
        ),
    ]