# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-19 12:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0009_auto_20161019_1242'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='category',
            order_with_respect_to='parent',
        ),
    ]
