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
    

# from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils import timezone
# from django.utils.translation import gettext_lazy as _


# class UserCustomManager(BaseUserManager):

#     use_in_migrations = True

#     def _create_user(self, phone_number, password, **extra_fields):
#         if not phone_number:
#             raise ValueError('The given phonenumber must be set')
#         user = self.model(phone_number=phone_number, username=phone_number, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, phone_number, password, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(phone_number, password, **extra_fields)

#     def create_superuser(self, phone_number, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(phone_number, password, **extra_fields)


# class User(AbstractUser):
#     # You have to remove 'username' and 'password'!
#     username = None
#     # password = None
#     email = models.EmailField(null=True, blank=True,unique=True)
#     is_superuser = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     phone_number = models.IntegerField(unique=True)
#     is_owner = models.BooleanField(default=False)
#     is_advisor = models.BooleanField(default=False)
#     name = models.CharField(max_length=40)
#     image = models.ImageField(blank=True, null=True)
#     data_join = models.DateTimeField(default=timezone.now)
#     code_agency = models.IntegerField(null=True, blank=True, default=0)

#     USERNAME_FIELD = 'email'
    
#     REQUIRED_FIELDS = []
    

#     objects = UserCustomManager()

#     class Meta:
#         verbose_name = 'user'
#         verbose_name_plural = 'users'


#     def create_user(self, email, password, **extra_fields):
#         """
#         Create and save a User with the given email and password.
#         """
#         if not email:
#             raise ValueError(_('The Email must be set'))
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user


#     def create_superuser(self, email, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(_('Superuser must have is_staff=True.'))
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True.'))
#         return self.create_user(email, password, **extra_fields)




