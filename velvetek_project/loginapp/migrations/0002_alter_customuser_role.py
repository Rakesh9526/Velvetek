# Generated by Django 5.1.4 on 2024-12-26 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('technician', 'Technician'), ('user', 'User')], default='user', max_length=20),
        ),
    ]