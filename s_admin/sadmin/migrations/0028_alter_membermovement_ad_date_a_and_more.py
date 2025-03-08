# Generated by Django 5.1.2 on 2025-02-21 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0027_alter_membermovement_mm_date_dr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membermovement',
            name='ad_date_a',
            field=models.DateTimeField(auto_now=True, help_text='Date record was last amended', null=True),
        ),
        migrations.AlterField(
            model_name='membermovement',
            name='ad_date_c',
            field=models.DateTimeField(auto_now_add=True, help_text='Date record was created', null=True),
        ),
        migrations.AlterField(
            model_name='membermovement',
            name='mm_dr_status',
            field=models.CharField(blank=True, choices=[('E', 'Expected'), ('S', 'Set'), ('P', 'Placed')], default='0', help_text='Status', max_length=1, null=True, verbose_name='Placed - Status'),
        ),
        migrations.AlterField(
            model_name='membermovement',
            name='mm_pk_status',
            field=models.CharField(blank=True, choices=[('W', 'Waiting'), ('S', 'Set'), ('P', 'Picked')], default='0', help_text='Status', max_length=1, null=True, verbose_name='Picked - Status'),
        ),
    ]
