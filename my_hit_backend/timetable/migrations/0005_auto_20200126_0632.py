# Generated by Django 3.0.2 on 2020-01-26 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0004_auto_20200126_0631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetable',
            old_name='image',
            new_name='file_name',
        ),
    ]
