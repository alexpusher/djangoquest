# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-19 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0007_auto_20161019_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.AddField(
            model_name='category',
            name='num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='top',
            name='num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]