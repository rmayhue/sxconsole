# Copyright (C) 2015-2016 Skylable Ltd. <info-copyright@skylable.com>
# License: GPLv2 or later, see LICENSE for more details.

# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 13:42
from __future__ import unicode_literals

from django.db import migrations
import sizefield.models
import sxconsole.core


class Migration(migrations.Migration):

    dependencies = [
        ('clusters', '0030_auto_20160920_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='size',
            field=sizefield.models.FileSizeField(null=True, validators=[sxconsole.core.size_validator], verbose_name='Size'),
        ),
    ]
