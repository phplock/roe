# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMDB', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mysqlcluster',
            name='defaultdb',
        ),
        migrations.AddField(
            model_name='mysqlcluster',
            name='foreign_ip',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='\u96c6\u7fa4\u5bf9\u5916IP'),
        ),
    ]
