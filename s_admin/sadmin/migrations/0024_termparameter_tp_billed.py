# Generated by Django 5.1.2 on 2024-12-29 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0023_alter_classbilling_cb_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='termparameter',
            name='tp_billed',
            field=models.CharField(choices=[('N', 'No'), ('Y', 'Yes')], default='N', help_text='Billed', max_length=1, verbose_name='Billed ?'),
        ),
    ]
