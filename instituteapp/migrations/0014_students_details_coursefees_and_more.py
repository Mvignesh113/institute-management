# Generated by Django 5.1.1 on 2024-11-13 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituteapp', '0013_students_details_pendingfees'),
    ]

    operations = [
        migrations.AddField(
            model_name='students_details',
            name='coursefees',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='students_details',
            name='coursename',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
