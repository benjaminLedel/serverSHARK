# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartshark', '0024_plugin_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='revision_hash',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
