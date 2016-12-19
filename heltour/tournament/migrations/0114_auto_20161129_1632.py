# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-29 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0113_auto_20161129_0415'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlternateSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('board_number', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')])),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.CharField(blank=True, choices=[('started', 'Started'), ('all_contacted', 'All alternates contacted')], max_length=31)),
                ('last_alternate_contact_date', models.DateTimeField(blank=True, null=True)),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Round')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Team')),
            ],
        ),
        migrations.RemoveField(
            model_name='playeravailability',
            name='alternate_status',
        ),
        migrations.AlterUniqueTogether(
            name='alternatesearch',
            unique_together=set([('round', 'team', 'board_number')]),
        ),
    ]