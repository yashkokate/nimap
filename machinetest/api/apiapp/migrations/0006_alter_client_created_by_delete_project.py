# Generated by Django 5.0.4 on 2024-04-17 11:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0005_client_created_at_client_created_by_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Client', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
