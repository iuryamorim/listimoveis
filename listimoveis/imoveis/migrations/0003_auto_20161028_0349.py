# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 03:49
from __future__ import unicode_literals

from django.db import migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0002_auto_20161027_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='photo',
            field=s3direct.fields.S3DirectField(blank=True),
        ),
    ]