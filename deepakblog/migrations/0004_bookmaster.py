# Generated by Django 3.1.6 on 2021-03-06 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepakblog', '0003_auto_20210304_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bookName', models.CharField(max_length=50, verbose_name='Book Name')),
                ('bookImage', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Upload Image')),
                ('bookDescription', models.CharField(max_length=250, verbose_name='Book Description')),
            ],
        ),
    ]
