from django.db import models
from django.db.models.fields import TextField
# Create your models here.

class Locate(models.Model):
    country = models.CharField(max_length=50, default="none", null=True)
    state = models.CharField(max_length=100, default="none", null=True)

class Brand(models.Model):
    bname = models.CharField(max_length=50)
    bdesc = models.TextField(max_length=500)
    bpic = models.ImageField(upload_to='images/brand/', height_field=None, width_field=None, max_length=None)
    bname_search_index = models.TextField(blank=True)
    locate = models.CharField(max_length=50, null=True, blank=True)
    country = models.ForeignKey(Locate, on_delete=models.CASCADE, related_name="brand_locate", null=True)

    def __str__(self):
        return self.bname

class Medium(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    website = models.TextField(null=True)
    ecsite = models.TextField( null=True )
    facebook = models.TextField(null=True)
    instagram = models.TextField(null=True)
    twitter = models.TextField(null=True)

    def __str__(self):
        return self.brand

class Type(models.Model):
    ptype = models.CharField(max_length=50)
    ptype_search_index = models.TextField(blank=True)
    ptype_color = models.CharField(max_length=50, default="greenyellow")

    def __str__(self):
        return self.ptype
    

class Product(models.Model):
    pname = models.CharField(max_length=50)
    ptype = models.ForeignKey(Type, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="brand_n")
    desc = models.TextField(max_length=500)
    ppic = models.ImageField(upload_to='images/product', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.pname
    