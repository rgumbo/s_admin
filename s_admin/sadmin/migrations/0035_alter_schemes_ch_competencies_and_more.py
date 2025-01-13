# Generated by Django 5.1.2 on 2025-01-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0034_rename_sf_email_staffmember_sf_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schemes',
            name='ch_competencies',
            field=models.CharField(blank=True, help_text='The competencies to be acquired', max_length=100, null=True, verbose_name='Competencies'),
        ),
        migrations.AlterField(
            model_name='schemes',
            name='ch_evaluation',
            field=models.CharField(blank=True, help_text='The Evaluation', max_length=100, null=True, verbose_name='Evaluation'),
        ),
        migrations.AlterField(
            model_name='schemes',
            name='ch_methods',
            field=models.CharField(blank=True, help_text='The methods to be used', max_length=100, null=True, verbose_name='Methods'),
        ),
        migrations.AlterField(
            model_name='schemes',
            name='ch_objectives',
            field=models.CharField(blank=True, help_text='The objectives for the period', max_length=100, null=True, verbose_name='Objetives'),
        ),
        migrations.AlterField(
            model_name='schemes',
            name='ch_references',
            field=models.CharField(blank=True, help_text='The sources of materials', max_length=100, null=True, verbose_name='Sources'),
        ),
        migrations.AlterField(
            model_name='schemes',
            name='ch_review2',
            field=models.CharField(blank=True, help_text='The second reviewer', max_length=100, null=True, verbose_name='Review2'),
        ),
        migrations.AlterField(
            model_name='schemes',
            name='ch_status',
            field=models.CharField(choices=[('0', 'New'), ('1', 'Done'), ('2', 'Pending'), ('3', 'Cancelled')], default='0', help_text='Status', max_length=1, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='schemes',
            name='ch_topic',
            field=models.CharField(blank=True, help_text='The Topic covered', max_length=100, null=True, verbose_name='Topic'),
        ),
        migrations.AlterField(
            model_name='schemes',
            name='ch_type',
            field=models.CharField(blank=True, choices=[('1', 'Academic'), ('2', 'Sport'), ('3', 'Extra Curricular')], help_text='Type of the Syllabus', max_length=1, null=True, verbose_name='Type'),
        ),
    ]
