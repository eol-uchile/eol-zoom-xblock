# Generated by Django 2.2.13 on 2020-09-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eolzoom', '0013_eolzoommappingusermeet_is_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='eolgoogleauth',
            name='custom_live_streaming_service',
            field=models.BooleanField(default=False),
        ),
    ]