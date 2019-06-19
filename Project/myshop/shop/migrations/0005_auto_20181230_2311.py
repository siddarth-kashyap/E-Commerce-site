# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brochure',
            field=models.FileField(null=True, upload_to='brochures/%Y/%M/%D/'),
        ),
    ]
