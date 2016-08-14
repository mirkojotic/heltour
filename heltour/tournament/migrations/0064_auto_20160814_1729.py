# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-14 17:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0063_season_tag'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='season',
            unique_together=set([('league', 'name'), ('league', 'tag')]),
        ),
    ]
