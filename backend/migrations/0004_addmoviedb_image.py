# Generated by Django 4.1.3 on 2023-01-18 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_addmoviedb'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmoviedb',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='Profile'),
        ),
    ]
