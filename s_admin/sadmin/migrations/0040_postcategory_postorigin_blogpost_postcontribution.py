# Generated by Django 5.1.2 on 2025-01-12 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0039_dailyplan_sp_finish_time_dailyplan_sp_start_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('ct_code', models.CharField(help_text='Enter code uniquely identifying post category', max_length=10, primary_key=True, serialize=False, verbose_name='Code')),
                ('ct_desc', models.CharField(blank=True, help_text='The description of the category', max_length=50, null=True)),
                ('ct_seo_title', models.CharField(blank=True, help_text='The SEO title of the blog', max_length=300, null=True, verbose_name='SEO Title')),
                ('ct_seo_desc', models.CharField(blank=True, help_text='The SEO description of the blog', max_length=250, null=True, verbose_name='SEO Description')),
                ('slug', models.SlugField(blank=True, help_text='The slug field for the blog for user facing title', max_length=250, unique=True)),
                ('ad_user_c', models.CharField(blank=True, help_text='The user creating the record', max_length=30, null=True)),
                ('ad_user_a', models.CharField(blank=True, help_text='The last amending user', max_length=30, null=True)),
                ('ad_date_c', models.DateTimeField(auto_now_add=True, help_text='Date record was created')),
                ('ad_date_a', models.DateTimeField(auto_now=True, help_text='Date record was last amended')),
                ('ad_device_c', models.CharField(blank=True, help_text='The Device creating the record', max_length=100, null=True)),
                ('ad_device_a', models.CharField(blank=True, help_text='The Last amending device', max_length=100, null=True)),
                ('ad_ipadress_c', models.CharField(blank=True, help_text='The record creating ip address', max_length=50, null=True)),
                ('ad_ipadress_a', models.CharField(blank=True, help_text='The last amending ip address', max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Blog Category',
                'ordering': ['ct_desc'],
            },
        ),
        migrations.CreateModel(
            name='PostOrigin',
            fields=[
                ('po_num', models.CharField(help_text='Enter code uniquely identifying originator of the post', max_length=10, primary_key=True, serialize=False, verbose_name='Code')),
                ('po_name', models.CharField(blank=True, help_text='The name of the originator', max_length=100, null=True)),
                ('po_position', models.CharField(blank=True, help_text='The position/title of the originator', max_length=50, null=True)),
                ('ad_user_c', models.CharField(blank=True, help_text='The user creating the record', max_length=30, null=True)),
                ('ad_user_a', models.CharField(blank=True, help_text='The last amending user', max_length=30, null=True)),
                ('ad_date_c', models.DateTimeField(auto_now_add=True, help_text='Date record was created')),
                ('ad_date_a', models.DateTimeField(auto_now=True, help_text='Date record was last amended')),
                ('ad_device_c', models.CharField(blank=True, help_text='The Device creating the record', max_length=100, null=True)),
                ('ad_device_a', models.CharField(blank=True, help_text='The Last amending device', max_length=100, null=True)),
                ('ad_ipadress_c', models.CharField(blank=True, help_text='The record creating ip address', max_length=50, null=True)),
                ('ad_ipadress_a', models.CharField(blank=True, help_text='The last amending ip address', max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'PostOrigin',
                'ordering': ['po_name'],
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('bp_num', models.AutoField(help_text='Number uniquely identifying the post', primary_key=True, serialize=False, verbose_name='Post Number')),
                ('bp_heading', models.CharField(help_text='The heading of the post', max_length=100, verbose_name='Heading')),
                ('bp_seo_title', models.CharField(blank=True, help_text='The SEO title of the blog', max_length=300, null=True, verbose_name='SEO Title')),
                ('bp_seo_desc', models.CharField(blank=True, help_text='The SEO description of the blog', max_length=250, null=True, verbose_name='SEO Description')),
                ('slug', models.SlugField(blank=True, help_text='The slug field for the blog for user facing title', max_length=250, unique=True)),
                ('bp_date', models.DateTimeField(auto_now_add=True, help_text='Date on which this post was created')),
                ('bp_body', models.TextField(help_text='The post s message', max_length=350, verbose_name='Message')),
                ('bp_status', models.CharField(choices=[('D', 'Draft'), ('R', 'Peered'), ('P', 'Publish')], default='D', help_text='Enter the status of the post', max_length=1, verbose_name='Status')),
                ('bp_file', models.FileField(blank=True, help_text='Choose File to upload', null=True, upload_to='media/', verbose_name='Attachment File')),
                ('bp_image', models.ImageField(blank=True, help_text='Choose image to upload', null=True, upload_to='media/', verbose_name='Image')),
                ('ad_user_c', models.CharField(blank=True, help_text='The user creating the record', max_length=30, null=True)),
                ('ad_user_a', models.CharField(blank=True, help_text='The last amending user', max_length=30, null=True)),
                ('ad_date_c', models.DateTimeField(auto_now_add=True, help_text='Date record was created')),
                ('ad_date_a', models.DateTimeField(auto_now=True, help_text='Date record was last amended')),
                ('ad_device_c', models.CharField(blank=True, help_text='The Device creating the record', max_length=100, null=True)),
                ('ad_device_a', models.CharField(blank=True, help_text='The Last amending device', max_length=100, null=True)),
                ('ad_ipadress_c', models.CharField(blank=True, help_text='The record creating ip address', max_length=50, null=True)),
                ('ad_ipadress_a', models.CharField(blank=True, help_text='The last amending ip address', max_length=50, null=True)),
                ('bp_ct_code', models.ForeignKey(help_text='Category into which this post falls', on_delete=django.db.models.deletion.CASCADE, to='sadmin.postcategory', verbose_name='Category')),
                ('bp_po_num', models.ForeignKey(help_text='The originator of the post', on_delete=django.db.models.deletion.CASCADE, to='sadmin.postorigin', verbose_name='Originator')),
            ],
            options={
                'verbose_name': 'Blog Post',
                'ordering': ['bp_date'],
            },
        ),
        migrations.CreateModel(
            name='PostContribution',
            fields=[
                ('pc_num', models.AutoField(help_text='Number uniquely identifying the contribution', primary_key=True, serialize=False, verbose_name='Contribution Number')),
                ('pc_contribution', models.TextField(help_text='The contribution to a post', max_length=350, verbose_name='Contribution')),
                ('pc_email', models.EmailField(blank=True, help_text='The contributor s email', max_length=254, null=True, verbose_name='Email')),
                ('pc_contributor', models.CharField(blank=True, help_text='The name of the contributor', max_length=50, null=True, verbose_name='Contributor')),
                ('pc_active', models.BooleanField(default=False, help_text='Indicates whether contribution is accepted or not', verbose_name='Accepted')),
                ('ad_user_c', models.CharField(blank=True, help_text='The Creating record', max_length=30, null=True)),
                ('ad_user_a', models.CharField(blank=True, help_text='The last amending user', max_length=30, null=True)),
                ('ad_date_c', models.DateTimeField(auto_now_add=True, help_text='Date record was created')),
                ('ad_date_a', models.DateTimeField(auto_now=True, help_text='Date record was last amended')),
                ('ad_device_c', models.CharField(blank=True, help_text='The Device creating the record', max_length=100, null=True)),
                ('ad_device_a', models.CharField(blank=True, help_text='The Last amending device', max_length=100, null=True)),
                ('ad_ipadress_c', models.CharField(blank=True, help_text='The record creating ip address', max_length=50, null=True)),
                ('ad_ipadress_a', models.CharField(blank=True, help_text='The last amending ip address', max_length=50, null=True)),
                ('pc_bp_num', models.ForeignKey(db_column='pc_bp_num', help_text='The Reference post for this contribution', on_delete=django.db.models.deletion.CASCADE, related_name='contributions', to='sadmin.blogpost', verbose_name='BlogPost')),
            ],
            options={
                'verbose_name': 'Contribution',
                'ordering': ['ad_date_c'],
            },
        ),
    ]
