# Generated by Django 5.1.1 on 2024-11-11 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituteapp', '0012_students_details_total_fees'),
    ]

    operations = [
        migrations.AddField(
            model_name='students_details',
            name='pendingfees',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
