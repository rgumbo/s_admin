# Generated by Django 5.1.2 on 2024-12-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0012_alter_learnerassessment_la_sb_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='schemes',
            name='ch_references',
            field=models.CharField(default=1, help_text='The sources of materials', max_length=100, verbose_name='Sources'),
            preserve_default=False,
        ),
    ]
