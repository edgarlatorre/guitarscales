# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scales', '0003_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['string', 'fret']},
        ),
        migrations.AddField(
            model_name='scale',
            name='slug',
            field=models.SlugField(default='test'),
            preserve_default=False,
        ),
    ]
