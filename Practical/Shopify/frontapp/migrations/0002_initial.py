# Generated by Django 4.2.1 on 2023-05-16 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('frontapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Handle', models.TextField(blank=True, null=True)),
                ('Title', models.TextField()),
                ('Body', models.TextField(blank=True, null=True)),
                ('Vendor', models.TextField(blank=True, null=True)),
                ('Type', models.TextField(blank=True, null=True)),
                ('Tags', models.TextField(blank=True, null=True)),
                ('Published', models.TextField(blank=True, null=True)),
                ('Option1_Name', models.TextField(blank=True, null=True)),
                ('Option1_Value', models.TextField(blank=True, null=True)),
                ('Option2_Name', models.TextField(blank=True, null=True)),
                ('Option2_Value', models.TextField(blank=True, null=True)),
                ('Option3_Name', models.TextField(blank=True, null=True)),
                ('Option3_Value', models.TextField(blank=True, null=True)),
                ('Variant_SKU', models.TextField(blank=True, null=True)),
                ('Variant_Grams', models.TextField(blank=True, null=True)),
                ('Variant_Inventory_Tracker', models.TextField(blank=True, null=True)),
                ('Variant_Inventory_Policy', models.TextField(blank=True, null=True)),
                ('Variant_Fulfillment_Service', models.TextField(blank=True, null=True)),
                ('Variant_Price', models.TextField(blank=True, null=True)),
                ('Variant_Compare_At_Price', models.TextField(blank=True, null=True)),
                ('Variant_Requires_Shipping', models.TextField(blank=True, null=True)),
                ('Variant_Taxable', models.TextField(blank=True, null=True)),
                ('Variant_Barcode', models.TextField(blank=True, null=True)),
                ('Image_Src', models.TextField(blank=True, null=True)),
                ('Image_Position', models.TextField(blank=True, null=True)),
                ('Image_Alt_Text', models.TextField(blank=True, null=True)),
                ('Gift_Card', models.TextField(blank=True, null=True)),
                ('SEO_Title', models.TextField(blank=True, null=True)),
                ('SEO_Description', models.TextField(blank=True, null=True)),
                ('Google_Shopping_Google_Product_Category', models.TextField(blank=True, null=True)),
                ('Google_Shopping_Gender', models.TextField(blank=True, null=True)),
                ('Google_Shopping_Age_Group', models.TextField(blank=True, null=True)),
                ('Google_Shopping_MPN', models.TextField(blank=True, null=True)),
                ('Google_Shopping_AdWords_Grouping', models.TextField(blank=True, null=True)),
                ('Google_Shopping_AdWords_Labels', models.TextField(blank=True, null=True)),
                ('Google_Shopping_Condition', models.TextField(blank=True, null=True)),
                ('Google_Shopping_Custom_Product', models.TextField(blank=True, null=True)),
                ('Google_Shopping_Custom_Label_0', models.TextField(blank=True, null=True)),
                ('Google_Shopping_Custom_Label_1', models.TextField(blank=True, null=True)),
                ('Google_Shopping_Custom_Label_2', models.TextField(blank=True, null=True)),
                ('Google_Shopping_Custom_Label_3', models.TextField(blank=True, null=True)),
                ('Google_Shopping_Custom_Label_4', models.TextField(blank=True, null=True)),
                ('Variant_Image', models.TextField(blank=True, null=True)),
                ('Variant_Weight_Unit', models.TextField(blank=True, null=True)),
                ('Variant_Tax_Code', models.TextField(blank=True, null=True)),
                ('Cost_per_item', models.TextField(blank=True, null=True)),
                ('Status', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_activity_date', models.DateTimeField(auto_now_add=True)),
                ('IP', models.TextField()),
                ('description', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_token', models.CharField(max_length=100)),
                ('time', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductWithUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Handle', models.TextField(blank=True, null=True)),
                ('Title', models.TextField()),
                ('Body', models.TextField(blank=True, null=True)),
                ('Vendor', models.TextField(blank=True, null=True)),
                ('Type', models.TextField(blank=True, null=True)),
                ('Tags', models.TextField(blank=True, null=True)),
                ('Published', models.TextField(blank=True, null=True)),
                ('Variant_SKU', models.TextField(blank=True, null=True)),
                ('Variant_Inventory_Tracker', models.TextField(blank=True, null=True)),
                ('Variant_Price', models.TextField(blank=True, null=True)),
                ('Image_Src', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exceptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exception_code', models.CharField(max_length=10)),
                ('exception_date', models.DateTimeField(auto_now_add=True)),
                ('exception_type', models.CharField(max_length=100)),
                ('messages', models.TextField()),
                ('IP', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
