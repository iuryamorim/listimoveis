# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 06:41
from __future__ import unicode_literals

from django.db import migrations, models
import listimoveis.imoveis.validators


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='cep',
            field=models.CharField(max_length=8, validators=[listimoveis.imoveis.validators.validate_cep], verbose_name='cep'),
        ),
    ]