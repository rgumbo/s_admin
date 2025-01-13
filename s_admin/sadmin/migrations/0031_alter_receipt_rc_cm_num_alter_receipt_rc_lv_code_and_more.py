# Generated by Django 5.1.2 on 2025-01-04 10:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0030_alter_memberrecord_mr_term_alter_receipt_rc_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='rc_cm_num',
            field=models.ForeignKey(blank=True, help_text='Learner', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rc_cm', to='sadmin.classmember', verbose_name='Member'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='rc_lv_code',
            field=models.ForeignKey(blank=True, help_text='The study Level', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mr_rc', to='sadmin.level', verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='rc_mr_num',
            field=models.CharField(default='0', help_text='The member transaction to which funds to be applied', max_length=20, verbose_name='Member Record'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='rc_pay_ref',
            field=models.CharField(blank=True, help_text='The payment reference', max_length=20, null=True, verbose_name='Payment Ref'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='rc_sc_code',
            field=models.ForeignKey(blank=True, help_text='The Class', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rc_sc', to='sadmin.schoolclass', verbose_name='School Class'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='rc_term',
            field=models.IntegerField(blank=True, help_text='Term for which the fees are considered', null=True, verbose_name='Period'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='rc_trans_date',
            field=models.DateTimeField(blank=True, help_text='Transaction Date', null=True, verbose_name='Transaction Date'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='rc_year',
            field=models.IntegerField(blank=True, help_text='Year for which the fees are considered', null=True, verbose_name='Year'),
        ),
    ]
