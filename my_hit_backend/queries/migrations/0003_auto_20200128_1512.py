# Generated by Django 3.0.2 on 2020-01-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0002_auto_20200128_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='status',
            field=models.CharField(choices=[('unread', 'unread'), ('read', 'read'), ('replied', 'replied')], default='unread', max_length=50),
        ),
    ]
