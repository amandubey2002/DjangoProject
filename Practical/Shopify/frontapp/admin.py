from django.contrib import admin
from .models import Profile, Product, Exceptions, UserActivity,Roleprofile

# Register your models here.


admin.site.register(Profile)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ["id"]

    class Meta:
        model = Product
        fields = ["id"]
        ordering = ("-id",)


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user_id",
        "exception_code",
        "exception_date",
        "exception_type",
        "messages",
        "IP",
    ]


admin.site.register(Exceptions, ProductAdmin)


class UserActivityAdmin(admin.ModelAdmin):
    list_display = ["id", "user_id", "user_activity_date", "IP", "description"]


admin.site.register(UserActivity, UserActivityAdmin)


class RoleprofileAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "is_admin", "is_staff", "is_active"]

admin.site.register(Roleprofile, RoleprofileAdmin)