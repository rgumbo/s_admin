# Generated by Django 5.1.2 on 2024-12-31 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0025_alter_classbilling_cb_lv_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberRecord',
            fields=[
                ('mr_num', models.AutoField(help_text='System generated number uniquely identifying a group member transaction', primary_key=True, serialize=False, verbose_name='Number')),
                ('mr_year', models.IntegerField(help_text='Year for which the fees are considered', verbose_name='Period')),
                ('mr_term', models.IntegerField(help_text='Term for which the fees are considered', verbose_name='Period')),
                ('mr_trans_date', models.DateTimeField(help_text='Transaction Date', verbose_name='Transaction Date')),
                ('mr_due_date', models.DateTimeField(blank=True, help_text='Transaction s due date', null=True, verbose_name='Due Date')),
                ('mr_pamount', models.DecimalField(decimal_places=2, default=0, help_text='The amount', max_digits=15, verbose_name='Projected Amount')),
                ('mr_aamount', models.DecimalField(decimal_places=2, default=0, help_text='The actual transaction amount', max_digits=15, verbose_name='Actual Amount')),
                ('mr_pay_ref', models.CharField(blank=True, help_text='The payment reference', max_length=20, null=True, verbose_name='Payment Ref')),
                ('mr_category', models.CharField(choices=[('1', 'Contributions'), ('2', 'Advances'), ('3', 'Interest'), ('4', 'Penalties'), ('G', 'General')], default='1', help_text='Category of the transaction', max_length=1, verbose_name='Category')),
                ('mr_dr_cr', models.CharField(default='D', help_text='The Transaction is a debit or a credit', max_length=1, verbose_name='Debit/Credit')),
                ('mr_paid', models.CharField(default='N', help_text='Indicates payment in settlement for this transaction', max_length=1, verbose_name='Paid')),
                ('mr_status', models.CharField(choices=[('1', 'Live'), ('2', 'Reversed'), ('3', 'Cancelled')], default='1', help_text='Status of the transaction', max_length=1, verbose_name='Status')),
                ('mr_processed', models.CharField(default='N', help_text='Indicates transaction has been processed', max_length=1, verbose_name='Processed')),
                ('mr_pay_type', models.CharField(blank=True, choices=[('1', 'Cheque'), ('2', 'Transfer'), ('3', 'Cash'), ('4', 'Mobile Money')], default='N', help_text='Payment type', max_length=1, null=True, verbose_name='Payment Type')),
                ('ad_user_c', models.CharField(blank=True, help_text='The user creating the record', max_length=30, null=True)),
                ('ad_user_a', models.CharField(blank=True, help_text='The last amending user', max_length=30, null=True)),
                ('ad_date_c', models.DateTimeField(auto_now_add=True, help_text='Date record was created', null=True)),
                ('ad_date_a', models.DateTimeField(auto_now=True, help_text='Date record was last amended', null=True)),
                ('ad_device_c', models.CharField(blank=True, help_text='The Device creating the record', max_length=100, null=True)),
                ('ad_device_a', models.CharField(blank=True, help_text='The Last amending device', max_length=100, null=True)),
                ('ad_ipadress_c', models.CharField(blank=True, help_text='The record creating ip address', max_length=50, null=True)),
                ('ad_ipadress_a', models.CharField(blank=True, help_text='The last amending ip address', max_length=50, null=True)),
                ('mr_cb_num', models.ForeignKey(help_text='Name of the fee', on_delete=django.db.models.deletion.CASCADE, related_name='mr_lv', to='sadmin.classbilling', verbose_name='Billing Head')),
                ('mr_cm_num', models.ForeignKey(help_text='Learner', on_delete=django.db.models.deletion.CASCADE, related_name='mr_cm', to='sadmin.classmember', verbose_name='Member')),
                ('mr_lv_code', models.ForeignKey(help_text='The study Level', on_delete=django.db.models.deletion.CASCADE, related_name='mr_lv', to='sadmin.level', verbose_name='Level')),
                ('mr_sc_code', models.ForeignKey(help_text='The Class', on_delete=django.db.models.deletion.CASCADE, related_name='mr_sc', to='sadmin.schoolclass', verbose_name='School Class')),
            ],
            options={
                'verbose_name': 'Member Record',
                'ordering': ['mr_num'],
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('rc_num', models.AutoField(help_text='System generated number uniquely identifying a receipt', primary_key=True, serialize=False, verbose_name='Number')),
                ('rc_mr_num', models.CharField(default=0, help_text='The member transaction to which funds to be applied', max_length=20, verbose_name='Member Record')),
                ('rc_period', models.IntegerField(help_text='Period in which transaction occurred', verbose_name='Period')),
                ('rc_trans_date', models.DateTimeField(help_text='Transaction Date', verbose_name='Transaction Date')),
                ('rc_value_date', models.DateTimeField(blank=True, help_text='Transaction s value date', null=True, verbose_name='Value Date')),
                ('rc_due_date', models.DateTimeField(blank=True, help_text='Transaction s due date', null=True, verbose_name='Due Date')),
                ('rc_pamount', models.DecimalField(decimal_places=2, default=0, help_text='The projected trans amount', max_digits=15, verbose_name='Projected Amount')),
                ('rc_aamount', models.DecimalField(decimal_places=2, default=0, help_text='The actual transaction amount', max_digits=15, verbose_name='Actual Amount')),
                ('rc_balance', models.DecimalField(decimal_places=2, default=0, help_text='The balance on the advance', max_digits=15, verbose_name='Balance')),
                ('rc_pay_ref', models.CharField(help_text='The payment reference', max_length=20, verbose_name='Payment Ref')),
                ('rc_dr_cr', models.CharField(default='D', help_text='The Transaction is a debit or a credit', max_length=1, verbose_name='Debit/Credit')),
                ('rc_paid', models.CharField(default='N', help_text='Indicates payment in settlement for this transaction', max_length=1, verbose_name='Paid')),
                ('rc_status', models.CharField(choices=[('1', 'Live'), ('2', 'Reversed'), ('3', 'Cancelled')], default='1', help_text='Status of the transaction', max_length=1, verbose_name='Status')),
                ('rc_processed', models.CharField(choices=[('1', 'Pending'), ('2', 'Processed')], default='N', help_text='Processed ?', max_length=1, verbose_name='Processed')),
                ('rc_pay_type', models.CharField(choices=[('1', 'Cheque'), ('2', 'Transfer'), ('3', 'Cash'), ('4', 'Mobile Money')], default='3', help_text='Payment type', max_length=1, verbose_name='Payment Type')),
                ('ad_user_c', models.CharField(blank=True, help_text='The user creating the record', max_length=30, null=True)),
                ('ad_user_a', models.CharField(blank=True, help_text='The last amending user', max_length=30, null=True)),
                ('ad_date_c', models.DateTimeField(auto_now_add=True, help_text='Date record was created')),
                ('ad_date_a', models.DateTimeField(auto_now=True, help_text='Date record was last amended')),
                ('ad_device_c', models.CharField(blank=True, help_text='The Device creating the record', max_length=100, null=True)),
                ('ad_device_a', models.CharField(blank=True, help_text='The Last amending device', max_length=100, null=True)),
                ('ad_ipadress_c', models.CharField(blank=True, help_text='The record creating ip address', max_length=50, null=True)),
                ('ad_ipadress_a', models.CharField(blank=True, help_text='The last amending ip address', max_length=50, null=True)),
                ('rc_cm_num', models.ForeignKey(help_text='Learner', on_delete=django.db.models.deletion.CASCADE, related_name='rc_cm', to='sadmin.classmember', verbose_name='Member')),
                ('rc_lv_code', models.ForeignKey(help_text='The study Level', on_delete=django.db.models.deletion.CASCADE, related_name='mr_rc', to='sadmin.level', verbose_name='Level')),
                ('rc_sc_code', models.ForeignKey(help_text='The Class', on_delete=django.db.models.deletion.CASCADE, related_name='rc_sc', to='sadmin.schoolclass', verbose_name='School Class')),
            ],
            options={
                'verbose_name': 'Receipt',
                'ordering': ['rc_num'],
            },
        ),
    ]
