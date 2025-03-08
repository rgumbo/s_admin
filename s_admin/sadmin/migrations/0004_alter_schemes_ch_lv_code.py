# Generated by Django 5.1.2 on 2025-01-26 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0003_dailyplan_sp_cs_code_alter_dailyplan_sp_lc_num_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schemes',
            name='ch_lv_code',
            field=models.ForeignKey(blank=True, help_text='The Study Level', null=True, on_delete=django.db.models.deletion.CASCADE, to='sadmin.level', verbose_name='Level'),
        ),
    ]
