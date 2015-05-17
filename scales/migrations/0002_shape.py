# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('number', models.IntegerField()),
                ('first_fret', models.IntegerField()),
                ('scale', models.ForeignKey(to='scales.Scale')),
            ],
        ),
    ]
