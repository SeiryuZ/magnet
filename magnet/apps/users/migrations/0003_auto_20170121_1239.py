# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.SmallIntegerField(choices=[(1, 'Volunteer'), (2, 'Initiator')], default=1),
        ),
    ]
