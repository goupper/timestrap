# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 22:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170615_2008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'default_permissions': ('view', 'add', 'change', 'delete'), 'ordering': ['-id']},
        ),
    ]