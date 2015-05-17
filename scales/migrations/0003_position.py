# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scales', '0002_shape'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('fret', models.IntegerField()),
                ('string', models.IntegerField()),
                ('finger', models.IntegerField()),
                ('is_root', models.BooleanField()),
                ('shape', models.ForeignKey(to='scales.Shape')),
            ],
        ),
    ]
