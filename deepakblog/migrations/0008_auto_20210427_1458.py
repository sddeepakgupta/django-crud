# Generated by Django 3.1.6 on 2021-04-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepakblog', '0007_auto_20210327_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmaster',
            name='price',
            field=models.IntegerField(default='20', verbose_name='Price Of The Book'),
        ),
    ]
