# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogs_log_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='para',
            field=models.CharField(max_length=100000, null=True),
        ),
    ]
