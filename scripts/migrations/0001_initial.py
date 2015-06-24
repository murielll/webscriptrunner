# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=150, null=True, blank=True)),
                ('visible', models.BooleanField(default=False)),
                ('filename', models.FileField(upload_to=b'scripts')),
            ],
        ),
    ]
