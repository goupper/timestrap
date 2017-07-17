# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('core', '0008_auto_20170709_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='sites',
            field=models.ManyToManyField(to='sites.Site'),
        ),
        migrations.AddField(
            model_name='task',
            name='sites',
            field=models.ManyToManyField(to='sites.Site'),
        ),
    ]