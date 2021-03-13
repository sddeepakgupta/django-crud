from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    content = RichTextField()
# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    instrument = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.first_name

class productType(models.Model):
    id = models.AutoField(primary_key=True)
    productType = models.CharField('Product Type', max_length=30)
    def __str__(self):
        return self.productType
class productCategories(models.Model):
    id = models.AutoField(primary_key=True)
    productType = models.ForeignKey(productType, on_delete=models.CASCADE)
    productcategorie = models.CharField('Product Categories', max_length=30)
    def __str__(self):
        return self.productcategorie 
class productMaster(models.Model):
    active = (
        ('1','Active'),
        ('0', 'Inactive')
    )
    id = models.AutoField(primary_key=True)
    productName = models.CharField('Product Name', max_length = 50)
    productType = models.ForeignKey(productType, on_delete=models.CASCADE)
    productCategories = models.ForeignKey(productCategories, on_delete=models.CASCADE)
    productPrize = models.IntegerField()
    productReleaseDate = models.DateField(max_length = 50)
    productProductImage = models.ImageField(null=True,blank=True, upload_to='uploads/')
    productDescription = RichTextUploadingField()
    active = models.CharField('Active', max_length=10, choices=active, blank=True)

class bookMaster(models.Model):
    id = models.AutoField(primary_key=True)
    bookName = models.CharField('Book Name', max_length = 50)
    bookImage = models.ImageField('Upload Image', null=True,blank=True, upload_to='uploads/')
    bookDescription = RichTextUploadingField('Book Description')    