# Generated by Django 5.1.1 on 2024-10-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituteapp', '0002_remove_students_details_name_students_details_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='students_details',
            name='idnum',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
