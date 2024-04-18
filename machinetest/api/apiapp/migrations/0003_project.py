# Generated by Django 4.2.5 on 2024-04-03 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_delete_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=50)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiapp.client')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiapp.user')),
            ],
        ),
    ]