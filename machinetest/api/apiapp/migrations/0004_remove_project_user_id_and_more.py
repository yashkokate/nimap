# Generated by Django 5.0.4 on 2024-04-08 10:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0003_project'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user_id',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='client_id',
            new_name='client',
        ),
        migrations.RemoveField(
            model_name='client',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='client',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='project',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='project',
            name='created_by',
        ),
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
