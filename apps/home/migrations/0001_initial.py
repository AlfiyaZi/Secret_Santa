# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('pw_hash', models.CharField(max_length=255)),
                ('admin', models.CharField(max_length=255)),
            ],
        ),
    ]
