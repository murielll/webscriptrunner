# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='args',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='script',
            name='interpreter',
            field=models.CharField(default=b'/bin/bash', max_length=150),
        ),
    ]
