# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20160205_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='santa',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
