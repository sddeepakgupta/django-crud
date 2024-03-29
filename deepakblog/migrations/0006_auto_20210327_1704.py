# Generated by Django 3.1.6 on 2021-03-27 11:34

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepakblog', '0005_auto_20210306_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmaster',
            name='price',
            field=models.IntegerField(default='20', editable=False, max_length=7, verbose_name='Price Of The Book'),
        ),
        migrations.AlterField(
            model_name='bookmaster',
            name='bookDescription',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Book Description'),
        ),
    ]
