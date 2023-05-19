from django.db import models

class Product(models.Model):
    Handle = models.CharField(max_length=400,null=True,blank=True)
    Title = models.CharField(max_length=400)
    Body = models.TextField(max_length=400,null=True,blank=True)
    Vendor = models.CharField(max_length=400,null=True,blank=True)
    Type = models.CharField(max_length=400,null=True,blank=True)
    Tags = models.CharField(max_length=400,null=True,blank=True)
    Published = models.CharField(max_length=400,null=True,blank=True)
    Variant_SKU = models.CharField(max_length=400,null=True,blank=True)
    Variant_Inventory_Tracker = models.CharField(max_length=400,null=True,blank=True)
    Variant_Price = models.CharField(max_length=400,null=True,blank=True)
    Image_Src = models.URLField(max_length=400,null=True,blank=True)


    def __str__(self):
        return self.Title