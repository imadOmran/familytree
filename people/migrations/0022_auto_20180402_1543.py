# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-02 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0021_auto_20180402_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Birth/Baptism'), (1, 'Marriage'), (2, 'Death/Burial'), (3, 'Census'), (4, 'Military'), (5, 'Land'), (6, 'Press'), (7, 'Emigration/Citizenship')]),
        ),
    ]
