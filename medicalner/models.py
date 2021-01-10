from django.db import models

# Create your models here.
class medicine(models.Model):

    sku_id      = models.CharField(max_length=10,blank=True,null=True)
    product_id  = models.CharField(max_length=10,blank=True,null=True)
    sku_name    = models.CharField(max_length=30,blank=True,null=True)
    price       = models.CharField(max_length=10,blank=True,null=True)
    manufacturer_name = models.CharField(max_length=30,blank=True,null=True)
    salt_name   = models.CharField(max_length=30,blank=True,null=True)
    drug_form   = models.CharField(max_length=30,blank=True,null=True)
    pack_size   = models.CharField(max_length=30,blank=True,null=True)
    strength    = models.CharField(max_length=30,blank=True,null=True)
    product_banned  = models.CharField(max_length=30,blank=True,null=True)
    unit        = models.CharField(max_length=30,blank=True,null=True)
    price_per_unit = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return self.sku_name
