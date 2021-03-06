# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2020-03-19 12:49


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eolzoom', '0002_auto_20200313_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eolzoomauth',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='eolzoom_user',
                to=settings.AUTH_USER_MODEL,
                unique=True),
        ),
    ]
