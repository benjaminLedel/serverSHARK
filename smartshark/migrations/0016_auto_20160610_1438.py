# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartshark', '0015_auto_20160609_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plugin',
            name='requires',
            field=models.ManyToManyField(blank=True, to='smartshark.Plugin'),
        ),
    ]
