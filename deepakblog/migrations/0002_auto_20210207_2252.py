# Generated by Django 3.1.6 on 2021-02-07 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deepakblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('productcategorie', models.CharField(max_length=30, verbose_name='Product Categories')),
            ],
        ),
        migrations.CreateModel(
            name='productType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('productType', models.CharField(max_length=30, verbose_name='Product Type')),
            ],
        ),
        migrations.CreateModel(
            name='productMaster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=50, verbose_name='Product Name')),
                ('productPrize', models.IntegerField()),
                ('productReleaseDate', models.DateField(max_length=50)),
                ('productProductImage', models.ImageField(upload_to='images/')),
                ('productDescription', models.CharField(max_length=255)),
                ('active', models.CharField(blank=True, choices=[('1', 'Active'), ('0', 'Inactive')], max_length=10, verbose_name='Active')),
                ('productCategories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deepakblog.productcategories')),
                ('productType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deepakblog.producttype')),
            ],
        ),
        migrations.AddField(
            model_name='productcategories',
            name='productType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deepakblog.producttype'),
        ),
    ]
