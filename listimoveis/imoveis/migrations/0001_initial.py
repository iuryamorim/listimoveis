# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 01:05
from __future__ import unicode_literals

from django.db import migrations, models
import listimoveis.imoveis.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('address', models.CharField(max_length=255, verbose_name='endereço')),
                ('cep', models.IntegerField(validators=[listimoveis.imoveis.validators.validate_cep], verbose_name='cep')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('photo', models.ImageField(upload_to='imovel/', verbose_name='foto')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
            ],
            options={
                'verbose_name_plural': 'imóveis',
                'verbose_name': 'imóvel',
                'ordering': ('-created_at',),
            },
        ),
    ]
