# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-15 18:40
from __future__ import unicode_literals

import conf.managers
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('core', '0009_auto_20170714_1635'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='client',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', conf.managers.CurrentSiteManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='task',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', conf.managers.CurrentSiteManager()),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='site',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='site',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
    ]