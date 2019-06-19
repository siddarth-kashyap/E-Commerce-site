# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20181229_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brochure',
            field=models.FileField(null=True, upload_to='brochures/%Y/%M/%D/', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/%Y/%M/%D', blank=True),
        ),
    ]
