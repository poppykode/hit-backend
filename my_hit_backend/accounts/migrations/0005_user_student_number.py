# Generated by Django 3.0.2 on 2020-02-05 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200127_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='student_number',
            field=models.CharField(default='H1601575F', max_length=255),
        ),
    ]
