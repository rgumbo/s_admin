# Generated by Django 5.1.2 on 2025-02-22 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0029_alter_membermovement_mm_date_dr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyplan',
            name='sp_sl_code',
            field=models.ForeignKey(blank=True, help_text='Level Class', null=True, on_delete=django.db.models.deletion.CASCADE, to='sadmin.schoollevel', verbose_name='School Class'),
        ),
        migrations.AddField(
            model_name='schemes',
            name='ch_sl_code',
            field=models.ForeignKey(blank=True, help_text='Level Class', null=True, on_delete=django.db.models.deletion.CASCADE, to='sadmin.schoollevel', verbose_name='School Class'),
        ),
    ]
