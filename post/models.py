from django.db import models
from users.models import User
from product.models import Brand, Product
from django.utils import timezone

# Create your models here.
class Favp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="faved_p_user")
    product = models.ForeignKey(Product , on_delete=models.CASCADE, related_name="fav_product")
    day = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['product', 'user'], name='unique_product')
        ]
        
class Favb(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="faved_b_user")
    brand = models.ForeignKey(Brand , on_delete=models.CASCADE, related_name="fav_brand")
    day = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['brand', 'user'], name='unique_brand')
        ]

class Drunk(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="drunk_user")
    product = models.ForeignKey(Product , on_delete=models.CASCADE, related_name="drunk_product")
    day = models.DateTimeField(auto_now=False, auto_now_add=True)
    com = models.TextField(max_length=140, null=True, blank=True, default="記録用(Just for recording)")
    rate = models.IntegerField(blank=True, null=True, default=3)

    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['product', 'user'], name='unique_drunk')
        ]

class PostOb(models.Model):
    favp = models.OneToOneField(Favp, on_delete=models.CASCADE, null=True, blank=True, related_name="fav_post")
    drunk = models.OneToOneField(Drunk, on_delete=models.CASCADE, null=True, blank=True)
    