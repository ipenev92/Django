# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-25 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0009_auto_20180525_1259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alliancecharacter',
            options={'ordering': ['character_class', 'character_name']},
        ),
        migrations.AlterModelOptions(
            name='hordecharacter',
            options={'ordering': ['character_class', 'character_name']},
        ),
    ]
