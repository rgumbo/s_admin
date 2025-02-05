# Generated by Django 5.1.2 on 2024-11-30 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0011_alter_learnerassessment_la_sb_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learnerassessment',
            name='la_sb_code',
            field=models.ForeignKey(blank=True, default=1, help_text='Subject of study', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='la_sb_key', to='sadmin.subject', verbose_name='Subject'),
        ),
    ]
