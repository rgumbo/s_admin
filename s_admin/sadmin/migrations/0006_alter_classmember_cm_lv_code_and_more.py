# Generated by Django 5.1.2 on 2025-01-26 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0005_alter_schemes_ch_ex_board_alter_schemes_ch_sy_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classmember',
            name='cm_lv_code',
            field=models.ForeignKey(blank=True, help_text='Foreign key to Level', null=True, on_delete=django.db.models.deletion.CASCADE, to='sadmin.level', verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='memberrecord',
            name='mr_lv_code',
            field=models.ForeignKey(blank=True, help_text='The study Level', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mr_lv', to='sadmin.level', verbose_name='Level'),
        ),
    ]
