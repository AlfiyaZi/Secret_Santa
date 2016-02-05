# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20151125_0012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item',
            new_name='asin',
        ),
        migrations.AddField(
            model_name='item',
            name='imgURL',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.CharField(default='10', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='title',
            field=models.CharField(default='title', max_length=255),
            preserve_default=False,
        ),
    ]
