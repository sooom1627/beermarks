from django.db import models
# Create your models here.

class Brand(models.Model):
    bname = models.CharField(max_length=50)
    bdesc = models.TextField(max_length=300)
    bpic = models.ImageField(upload_to='images/brand/', height_field=None, width_field=None, max_length=None)
    bname_search_index = models.TextField(blank=True)
    
    def __str__(self):
        return self.bname

class Type(models.Model):
    ptype = models.CharField(max_length=50)
    ptype_search_index = models.TextField(blank=True)

    def __str__(self):
        return self.ptype
    

class Product(models.Model):
    pname = models.CharField(max_length=50)
    ptype = models.ForeignKey(Type, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    desc = models.TextField(max_length=200)
    ppic = models.ImageField(upload_to='images/product', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.pname
    