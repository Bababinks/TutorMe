# Generated by Django 4.1.7 on 2023-04-23 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorMe', '0013_alter_notification_student_alter_notification_tutor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifyTutor', to='tutorMe.tutormeuser'),
        ),
    ]
