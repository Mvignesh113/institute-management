# Generated by Django 5.1.1 on 2024-11-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituteapp', '0011_delete_fees_payment_delete_fees_report_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='students_details',
            name='total_fees',
            field=models.FloatField(default=0.0),
        ),
    ]
