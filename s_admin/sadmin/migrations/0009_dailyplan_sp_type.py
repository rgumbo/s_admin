# Generated by Django 5.1.2 on 2024-11-25 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0008_schemes_ch_sf_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyplan',
            name='sp_type',
            field=models.CharField(choices=[('1', 'Academic'), ('2', 'Sport'), ('3', 'Extra Curricular')], default='1', help_text='Type', max_length=1, verbose_name='Type'),
        ),
    ]
