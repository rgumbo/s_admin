# Generated by Django 5.1.2 on 2024-12-29 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0024_termparameter_tp_billed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classbilling',
            name='cb_lv_code',
            field=models.ForeignKey(blank=True, help_text='Foreign key to Level', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cb_lv', to='sadmin.level', verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='classbilling',
            name='cb_sc_code',
            field=models.ForeignKey(blank=True, help_text='Foreign key to SchoolClass', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cb_sc', to='sadmin.schoolclass', verbose_name='School Class'),
        ),
        migrations.AlterField(
            model_name='classbilling',
            name='cb_term',
            field=models.IntegerField(blank=True, help_text='The term of the year of study', null=True, verbose_name='Term'),
        ),
        migrations.AlterField(
            model_name='classbilling',
            name='cb_year',
            field=models.CharField(blank=True, help_text='Study Year', max_length=4, null=True, verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='subjectbilling',
            name='jb_lc_num',
            field=models.ForeignKey(blank=True, help_text='Foreign key to Level Class', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jb_lc', to='sadmin.levelclass', verbose_name='Level Class'),
        ),
        migrations.AlterField(
            model_name='subjectbilling',
            name='jb_lv_code',
            field=models.ForeignKey(blank=True, help_text='Foreign key to Level', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jb_lv', to='sadmin.level', verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='subjectbilling',
            name='jb_sb_code',
            field=models.ForeignKey(blank=True, help_text='Foreign key to Subject', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jb_sb', to='sadmin.subject', verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='subjectbilling',
            name='jb_sc_code',
            field=models.ForeignKey(blank=True, help_text='Foreign key to SchoolClass', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jb_sc', to='sadmin.schoolclass', verbose_name='School Class'),
        ),
        migrations.AlterField(
            model_name='subjectbilling',
            name='jb_term',
            field=models.IntegerField(blank=True, help_text='The term of the year of study', null=True, verbose_name='Term'),
        ),
        migrations.AlterField(
            model_name='subjectbilling',
            name='jb_year',
            field=models.CharField(blank=True, help_text='Study Year', max_length=4, null=True, verbose_name='Year'),
        ),
    ]
