# Generated by Django 5.1.4 on 2024-12-27 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=15, unique=True)),
                ('whatsapp_number', models.CharField(max_length=15)),
                ('reffered_by', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]