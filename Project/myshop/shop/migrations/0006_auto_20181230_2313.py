# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20181230_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brochure',
            field=models.FileField(upload_to='brochures/%Y/%M/%D', null=True, blank=True),
        ),
    ]
