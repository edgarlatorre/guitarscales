# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scales', '0004_add_slug_field_to_scale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scale',
            name='slug',
            field=models.SlugField(unique=True, blank=True),
        ),
    ]
