# Generated by Django 5.1.2 on 2025-01-27 10:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0008_subjectbilling_jb_sl_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classassessment',
            name='as_lc_num',
            field=models.ForeignKey(blank=True, help_text='The Level Class', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='level_key', to='sadmin.levelclass', verbose_name='Level Class'),
        ),
        migrations.AlterField(
            model_name='learnerassessment',
            name='la_lc_num',
            field=models.ForeignKey(blank=True, help_text='The Level Class', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='la_lc_key', to='sadmin.levelclass', verbose_name='Level Class'),
        ),
    ]
