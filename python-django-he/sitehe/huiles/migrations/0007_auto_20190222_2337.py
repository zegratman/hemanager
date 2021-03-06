# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-02-22 22:37
from __future__ import unicode_literals

from django.db import migrations, models
import huiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('huiles', '0006_auto_20190222_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='huileessentielle',
            name='famille_1_pct',
            field=models.IntegerField(default=0, validators=[huiles.models.percentage_validator], verbose_name='primaire %'),
        ),
        migrations.AlterField(
            model_name='huileessentielle',
            name='famille_2_pct',
            field=models.IntegerField(blank=True, default=0, validators=[huiles.models.percentage_validator], verbose_name='secondaire %'),
        ),
        migrations.AlterField(
            model_name='huileessentielle',
            name='famille_3_pct',
            field=models.IntegerField(blank=True, default=0, validators=[huiles.models.percentage_validator], verbose_name='tertiaire %'),
        ),
        migrations.AlterField(
            model_name='huileessentielle',
            name='famille_4_pct',
            field=models.IntegerField(blank=True, default=0, validators=[huiles.models.percentage_validator], verbose_name='annexe 1 %'),
        ),
        migrations.AlterField(
            model_name='huileessentielle',
            name='famille_5_pct',
            field=models.IntegerField(blank=True, default=0, validators=[huiles.models.percentage_validator], verbose_name='annexe 2 %'),
        ),
    ]
