# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import badger.models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('badger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(base_url=b'/media/uploads/', location=b'/home/donb/Documentos/TG/Services/uploads/uploads'), null=True, upload_to=badger.models.UploadTo(b'image', b'png'), blank=True),
        ),
        migrations.AlterField(
            model_name='badge',
            name='image',
            field=models.ImageField(help_text=b'Upload an image to represent the badge', storage=django.core.files.storage.FileSystemStorage(base_url=b'/media/uploads/', location=b'/home/donb/Documentos/TG/Services/uploads/uploads'), null=True, upload_to=badger.models.UploadTo(b'image', b'png'), blank=True),
        ),
        migrations.AlterField(
            model_name='deferredaward',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, null=True, blank=True),
        ),
    ]
