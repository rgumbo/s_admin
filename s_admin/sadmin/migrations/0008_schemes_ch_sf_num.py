# Generated by Django 5.1.2 on 2024-11-25 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0007_alter_classmember_cm_surname_memberregister'),
    ]

    operations = [
        migrations.AddField(
            model_name='schemes',
            name='ch_sf_num',
            field=models.ForeignKey(default=1, help_text='Staff member assigned', on_delete=django.db.models.deletion.CASCADE, to='sadmin.staffmember', verbose_name='Staff Member'),
            preserve_default=False,
        ),
    ]
