# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-02-05 05:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checker', '0007_document_credits'),
    ]

    operations = [
        migrations.CreateModel(
            name='credits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credits', models.DecimalField(decimal_places=0, default='1000', max_digits=8)),
                ('userr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
