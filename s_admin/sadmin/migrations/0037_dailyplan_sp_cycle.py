# Generated by Django 5.1.2 on 2025-01-11 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0036_alter_dailyplan_sp_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyplan',
            name='sp_cycle',
            field=models.IntegerField(blank=True, help_text='Cycle of the session', null=True, verbose_name='Cycle'),
        ),
    ]
