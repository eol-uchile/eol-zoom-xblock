# Generated by Django 2.2.13 on 2020-08-12 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eolzoom', '0008_auto_20200805_2109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eolgoogleauth',
            old_name='credendials',
            new_name='credentials',
        ),
    ]
