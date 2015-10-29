# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badger', '0002_auto_20150916_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='points_end',
            field=models.FloatField(default=0, help_text=b'points with the badge is awarded'),
        ),
    ]
