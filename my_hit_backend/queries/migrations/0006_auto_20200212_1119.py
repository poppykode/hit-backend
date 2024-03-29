# Generated by Django 3.0.2 on 2020-02-12 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('queries', '0005_auto_20200205_0956'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='query',
            options={'ordering': ['-timestamp'], 'verbose_name_plural': 'Queries'},
        ),
        migrations.AddField(
            model_name='query',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
