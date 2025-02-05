# Generated by Django 5.1.2 on 2025-01-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0038_termparameter_tp_cycledays'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyplan',
            name='sp_finish_time',
            field=models.TimeField(blank=True, help_text='Finishing Time', null=True, verbose_name='Finish Time'),
        ),
        migrations.AddField(
            model_name='dailyplan',
            name='sp_start_time',
            field=models.TimeField(blank=True, help_text='Starting Time', null=True, verbose_name='Start Time'),
        ),
    ]
