# Generated by Django 5.2.1 on 2025-06-23 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('file_data', models.TextField()),
            ],
        ),
    ]
