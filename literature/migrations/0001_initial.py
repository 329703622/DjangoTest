# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name='\u6807\u9898')),
                ('author', models.CharField(max_length=128, verbose_name='\u4f5c\u8005')),
                ('date', models.DateField(default=b'2000-01-01', verbose_name='\u5e74\u4efd')),
                ('source', models.CharField(max_length=128, verbose_name='\u51fa\u5904')),
            ],
        ),
    ]
