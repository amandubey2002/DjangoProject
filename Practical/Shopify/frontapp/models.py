from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_token = models.CharField(max_length=100)
    time = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.user)
    



class Product(models.Model):
    Handle = models.TextField(null=True,blank=True)
    Title = models.TextField()
    Body = models.TextField(null=True,blank=True)
    Vendor = models.TextField(null=True,blank=True)
    Type = models.TextField(null=True,blank=True)
    Tags = models.TextField(null=True,blank=True)
    Published = models.TextField(null=True,blank=True)
    Option1_Name= models.TextField(null=True,blank=True)
    Option1_Value= models.TextField(null=True,blank=True)
    Option2_Name= models.TextField(null=True,blank=True)
    Option2_Value= models.TextField(null=True,blank=True)
    Option3_Name= models.TextField(null=True,blank=True)
    Option3_Value= models.TextField(null=True,blank=True)
    Variant_SKU = models.TextField(null=True,blank=True)
    Variant_Grams= models.TextField(null=True,blank=True)
    Variant_Inventory_Tracker = models.TextField(null=True,blank=True)
    Variant_Inventory_Policy= models.TextField(null=True,blank=True)
    Variant_Fulfillment_Service= models.TextField(null=True,blank=True)
    Variant_Price = models.TextField(null=True,blank=True)
    Variant_Compare_At_Price= models.TextField(null=True,blank=True)
    Variant_Requires_Shipping= models.TextField(null=True,blank=True)
    Variant_Taxable= models.TextField(null=True,blank=True)
    Variant_Barcode= models.TextField(null=True,blank=True)
    Image_Src = models.TextField(null=True,blank=True)
    Image_Position= models.TextField(null=True,blank=True)
    Image_Alt_Text= models.TextField(null=True,blank=True)
    Gift_Card= models.TextField(null=True,blank=True)
    SEO_Title= models.TextField(null=True,blank=True)
    SEO_Description= models.TextField(null=True,blank=True)
    Google_Shopping_Google_Product_Category= models.TextField(null=True,blank=True)
    Google_Shopping_Gender= models.TextField(null=True,blank=True)
    Google_Shopping_Age_Group= models.TextField(null=True,blank=True)
    Google_Shopping_MPN= models.TextField(null=True,blank=True)
    Google_Shopping_AdWords_Grouping= models.TextField(null=True,blank=True)
    Google_Shopping_AdWords_Labels= models.TextField(null=True,blank=True)
    Google_Shopping_Condition= models.TextField(null=True,blank=True)
    Google_Shopping_Custom_Product= models.TextField(null=True,blank=True)
    Google_Shopping_Custom_Label_0= models.TextField(null=True,blank=True)
    Google_Shopping_Custom_Label_1= models.TextField(null=True,blank=True)
    Google_Shopping_Custom_Label_2= models.TextField(null=True,blank=True)
    Google_Shopping_Custom_Label_3= models.TextField(null=True,blank=True)
    Google_Shopping_Custom_Label_4= models.TextField(null=True,blank=True)
    Variant_Image= models.TextField(null=True,blank=True)
    Variant_Weight_Unit= models.TextField(null=True,blank=True)
    Variant_Tax_Code= models.TextField(null=True,blank=True)
    Cost_per_item= models.TextField(null=True,blank=True)
    Status= models.TextField(null=True,blank=True)
    is_delete = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.id} , {self.Title}"
    


class Exceptions(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    exception_code = models.CharField(max_length=10)
    exception_date = models.DateTimeField(auto_now_add=True)
    exception_type = models.CharField(max_length=100)
    messages = models.TextField()
    IP = models.TextField()
    
    
    def __str__(self):
        return f"{self.id} - {str(self.user_id)}"
        


class UserActivity(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    user_activity_date = models.DateTimeField(auto_now_add=True)
    IP = models.TextField()
    description = models.TextField()
    
    
    def __str__(self):
        return f"{self.id}"
        
    
    