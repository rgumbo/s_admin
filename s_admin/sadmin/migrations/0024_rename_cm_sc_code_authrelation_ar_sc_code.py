# Generated by Django 5.1.2 on 2025-02-18 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0023_membermovement_mm_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authrelation',
            old_name='cm_sc_code',
            new_name='ar_sc_code',
        ),
    ]
