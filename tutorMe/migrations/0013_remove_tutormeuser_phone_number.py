# Generated by Django 4.1.7 on 2023-04-26 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorMe', '0012_tutormeuser_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutormeuser',
            name='phone_number',
        ),
    ]