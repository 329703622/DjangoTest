# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='date',
            field=models.CharField(max_length=10, verbose_name='\u5e74\u4efd'),
        ),
    ]
