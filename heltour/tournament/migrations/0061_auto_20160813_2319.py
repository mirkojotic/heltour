# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-13 23:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0060_auto_20160813_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loneplayerpairing_old',
            name='player_pairing',
        ),
        migrations.RemoveField(
            model_name='loneplayerpairing_old',
            name='round',
        ),
        migrations.AlterUniqueTogether(
            name='teamplayerpairing_old',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='teamplayerpairing_old',
            name='player_pairing',
        ),
        migrations.RemoveField(
            model_name='teamplayerpairing_old',
            name='team_pairing',
        ),
        migrations.DeleteModel(
            name='LonePlayerPairing_old',
        ),
        migrations.DeleteModel(
            name='TeamPlayerPairing_old',
        ),
    ]