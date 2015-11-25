# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20151124_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'items',
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.ForeignKey(to='home.Item')),
            ],
            options={
                'db_table': 'wishlist',
            },
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(to='home.User'),
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(to='home.User'),
        ),
    ]
