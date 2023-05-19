from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from userapp.password_forgot import forgot_password
import uuid
from .models import Product
import threading
import csv
import threading
import pandas as pd
from rest_framework.generics import ListAPIView
from .serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from django.core.paginator import Paginator
import codecs
import datetime
from io import BytesIO
import csv
from datetime import datetime, timedelta
import threading
import logging
from .task import send_mail_to_user,permanent_delete_product
from django.contrib.auth.decorators import login_required
from .models import Exceptions, UserActivity
import socket


## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)


logger = logging.getLogger(__name__)
date = datetime.now()


def save_exception_to_database(user_id, exception_code, exception_type, message, ip):
    user_id_instence = User.objects.get(id=user_id)
    exception_log = Exceptions(
        user_id=user_id_instence,
        exception_code=exception_code,
        exception_date=date,
        exception_type=exception_type,
        messages=message,
        IP=ip,
    )
    exception_log.save()


def track_user_activity(user, ip_address, description):
    activity = UserActivity(user_id=user, IP=ip_address, description=description)
    activity.save()


# implement threading 
def import_csv_file(filename):
    # csvfile = BytesIO(filename)
    csvfile = BytesIO(filename)
    csvfile = codecs.iterdecode(csvfile, "utf-8")
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    import time
    time1 = time.perf_counter()

    for row in reader:
        (
            Handle,
            Title,
            Body,
            Vendor,
            Type,
            Tags,
            Published,
            Option1_Name,
            Option1_Value,
            Option2_Name,
            Option2_Value,
            Option3_Name,
            Option3_Value,
            Variant_SKU,
            Variant_Grams,
            Variant_Inventory_Tracker,
            Variant_Inventory_Policy,
            Variant_Fulfillment_Service,
            Variant_Price,
            Variant_Compare_At_Price,
            Variant_Requires_Shipping,
            Variant_Taxable,
            Variant_Barcode,
            Image_Src,
            Image_Position,
            Image_Alt_Text,
            Gift_Card,
            SEO_Title,
            SEO_Description,
            Google_Shopping_Google_Product_Category,
            Google_Shopping_Gender,
            Google_Shopping_Age_Group,
            Google_Shopping_MPN,
            Google_Shopping_AdWords_Grouping,
            Google_Shopping_AdWords_Labels,
            Google_Shopping_Condition,
            Google_Shopping_Custom_Product,
            Google_Shopping_Custom_Label_0,
            Google_Shopping_Custom_Label_1,
            Google_Shopping_Custom_Label_2,
            Google_Shopping_Custom_Label_3,
            Google_Shopping_Custom_Label_4,
            Variant_Image,
            Variant_Weight_Unit,
            Variant_Tax_Code,
            Cost_per_item,
            Status,
        ) = row

        # Create a new Person instance
        person = Product(
            Handle=Handle,
            Title=Title,
            Body=Body,
            Vendor=Vendor,
            Type=Type,
            Tags=Tags,
            Published=Published,
            Option1_Name=Option1_Name,
            Option1_Value=Option1_Value,
            Option2_Name=Option2_Name,
            Option2_Value=Option2_Value,
            Option3_Name=Option3_Name,
            Option3_Value=Option3_Value,
            Variant_SKU=Variant_SKU,
            Variant_Grams=Variant_Grams,
            Variant_Inventory_Tracker=Variant_Inventory_Tracker,
            Variant_Inventory_Policy=Variant_Inventory_Policy,
            Variant_Fulfillment_Service=Variant_Fulfillment_Service,
            Variant_Price=Variant_Price,
            Variant_Compare_At_Price=Variant_Compare_At_Price,
            Variant_Requires_Shipping=Variant_Requires_Shipping,
            Variant_Taxable=Variant_Taxable,
            Variant_Barcode=Variant_Barcode,
            Image_Src=Image_Src,
            Image_Position=Image_Position,
            Image_Alt_Text=Image_Alt_Text,
            Gift_Card=Gift_Card,
            SEO_Title=SEO_Title,
            SEO_Description=SEO_Description,
            Google_Shopping_Google_Product_Category=Google_Shopping_Google_Product_Category,
            Google_Shopping_Gender=Google_Shopping_Gender,
            Google_Shopping_Age_Group=Google_Shopping_Age_Group,
            Google_Shopping_MPN=Google_Shopping_MPN,
            Google_Shopping_AdWords_Grouping=Google_Shopping_AdWords_Grouping,
            Google_Shopping_AdWords_Labels=Google_Shopping_AdWords_Labels,
            Google_Shopping_Condition=Google_Shopping_Condition,
            Google_Shopping_Custom_Product=Google_Shopping_Custom_Product,
            Google_Shopping_Custom_Label_0=Google_Shopping_Custom_Label_0,
            Google_Shopping_Custom_Label_1=Google_Shopping_Custom_Label_1,
            Google_Shopping_Custom_Label_2=Google_Shopping_Custom_Label_2,
            Google_Shopping_Custom_Label_3=Google_Shopping_Custom_Label_3,
            Google_Shopping_Custom_Label_4=Google_Shopping_Custom_Label_4,
            Variant_Image=Variant_Image,
            Variant_Weight_Unit=Variant_Weight_Unit,
            Variant_Tax_Code=Variant_Tax_Code,
            Cost_per_item=Cost_per_item,
            Status=Status,
        )
        print("we hereeeeeeeeeeeeeeeeeeeeee")
        person.save()
    time2 = time.perf_counter()
    print(time2-time1)
        


def import_data_from_csv(filename):
    t = threading.Thread(target=import_csv_file, args=(filename,))
    t.start()
    t.join()


@login_required
def import_csv_with_thread(request):
    if request.method == "POST":
        file = request.FILES["csv_file"]
        print(file)
        file_data = file.read()
        import_data_from_csv(file_data)
        messages.success(request, "Data Imported successfully")

        return redirect("product_list_page")

    else:
        return render(request, "temp/import_csv.html")


@login_required(login_url="login")
def export_csv(request):
    try:
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        data = pd.DataFrame(serializer.data)
        print(data)
        buffer = BytesIO()
        # Write the DataFrame to the BytesIO object as an Excel file
        data.to_csv(buffer, index=False)
        # Set the buffer's file pointer at the beginning
        buffer.seek(0)
        # Create a response object with appropriate content type and headers
        response = HttpResponse(buffer.getvalue(), content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="products.csv"'
        messages.success(request, "Exported CSV successfully")
        user_id_instence = User.objects.get(id=request.user.id)
        description = {"messages": "This user try to Expot CSV", "data": request.POST}
        activity = UserActivity(
            user_id=user_id_instence,
            IP=ip_address,
            description=f"this is username {request.user.username} and {description}",
        )
        activity.save()
        print(response)
        return response

    except Exception as e:
        print("something went wrong")
        save_exception_to_database(request.user.id, "40", type(e), str(e), ip_address)

    return render(request, "temp/export_csv.html")


@login_required(login_url="login")
def import_pdf(request):
    return render(request, "temp/export_pdf.html")


@login_required(login_url="login")
def export_csv1(request):
    return render(request, "temp/export_csv.html")


def render_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="pdffile.pdf"'
    pdf_status = pisa.CreatePDF(html, dest=response)

    if pdf_status.err:
        return HttpResponse("Some errors were encountered <pre>" + html + "</pre>")

    return response


@login_required(login_url="login")
def generate_pdf(request):
    try:
        template_name = "temp/pdf_data.html"
        records = Product.objects.all()
        user_id_instence = User.objects.get(id=request.user.id)
        description = {"messages": "This user try to export pdf", "data": request.POST}
        activity = UserActivity(
            user_id=user_id_instence,
            IP=ip_address,
            description=f"this is username {request.user.username} and {description}",
        )
        activity.save()

        return render_pdf(
            template_name,
            {
                "Products": records,
            },
        )
    except Exception as e:
        print("something went wrong")
        save_exception_to_database(request.user.id, "40", type(e), str(e), ip_address)


# product list with pagination
@login_required(login_url="login")
def ProductList(request):
    try:
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        paginator = Paginator(queryset, 21)
        page_number = request.GET.get("page")
        final = paginator.get_page(page_number)
        lastpage = final.paginator.num_pages

        return render(
            request, "temp/product_list_page.html", {"data": final, "lastpage": lastpage}
        )

    except Exception as e:
        print("something went wrong")
        save_exception_to_database(request.user.id, "40", type(e), str(e), ip_address)


# for single delete
@login_required(login_url="login")
def delete_product(request, pk):
    try:
        queryset = Product.objects.get(id=pk)
        queryset.delete()
        messages.success(request, "Product has been deleted successfully")
        user_id_instence = User.objects.get(id=request.user.id)
        description = {
            "messages": "This user try to delete product",
            "data": request.POST,
        }
        activity = UserActivity(
            user_id=user_id_instence,
            IP=ip_address,
            description=f"this is username {request.user.username} and {description}",
        )
        activity.save()

        return redirect("product_list_page")

    except Exception as e:
        print("something went wrong")
        save_exception_to_database(request.user.id, "40", type(e), str(e), ip_address)



# send mail to all the reister user
@login_required(login_url="login")
def send_mail_to_all_users(request):
    scheduled_time = datetime.now() + timedelta(hours=1)
    send_mail_to_user.apply_async(eta=scheduled_time)
    messages.success(request, "Mail sent successfully")
    user_id_instence = User.objects.get(id=request.user.id)
    description = {
        "messages": "This user try to send mail to all user",
        "data": request.POST,
    }
    activity = UserActivity(
        user_id=user_id_instence,
        IP=ip_address,
        description=f"this is username {request.user.username} and {description}",
    )
    activity.save()

    return render(request, "temp/product_list_page.html")


@login_required(login_url="login")
def create_product(request):
    try:
        if request.method == "POST":
            user_id = request.POST.get("user")
            Handle = request.POST.get("handle")
            Title = request.POST.get("title")
            Body = request.POST.get("body")
            Vendor = request.POST.get("vendor")
            Type = request.POST.get("type")
            Tags = request.POST.get("tags")
            Published = request.POST.get("published")
            Variant_SKU = request.POST.get("variant_sku")
            Variant_Inventory_Tracker = request.POST.get("variant_inventory_tracker")
            Variant_Price = request.POST.get("variant_price")
            Image_Src = request.POST.get("img_src")
            # user = User.objects.get(id=user_id)
            print("we hereeeeeeeeeeeeeeeee")
            products = Product(
                Handle=Handle,
                Title=Title,
                Body=Body,
                Vendor=Vendor,
                Type=Type,
                Tags=Tags,
                Published=Published,
                Variant_SKU=Variant_SKU,
                Variant_Inventory_Tracker=Variant_Inventory_Tracker,
                Variant_Price=Variant_Price,
                Image_Src=Image_Src,
            )
            products.save()
            messages.success(request, "Product Add SucsessFullyyyyy")
            user_id_instence = User.objects.get(id=request.user.id)
            description = {
                "messages": "This user try to add product",
                "data": request.POST,
            }
            activity = UserActivity(
                user_id=user_id_instence,
                IP=ip_address,
                description=f"this is username {request.user.username} and {description}",
            )
            activity.save()
        return render(request, "temp/create_product.html")

    except Exception as e:
        print("something went wrong")
        save_exception_to_database(request.user.id, "40", type(e), str(e), ip_address)

    return render(request, "temp/create_product.html")


@login_required(login_url="login")
def product_list_page(request):
    try:
        if request.method == "POST":
            selected_ids = request.POST.getlist("selected_products")
            if selected_ids == []:
                messages.success(
                    request,
                    "No data has been choosen for deleting products please select first",
                )

                return redirect("product_list_page")

            else:
                print(selected_ids)
                Product.objects.filter(id__in=selected_ids).delete()
                messages.success(
                    request, f"Product id  {selected_ids} has been deleted successfully"
                )
                user_id_instence = User.objects.get(id=request.user.id)
                description = {
                    "messages": "This user try to delete product",
                    "data": request.POST,
                }
                activity = UserActivity(
                    user_id=user_id_instence,
                    IP=ip_address,
                    description=f"this is username {request.user.username} and {description}",
                )
                activity.save()

                return redirect("product_list_page")

        else:
            products = Product.objects.filter(is_delete=False)
            print(len(products))
            paginator = Paginator(products, 21)
            page_number = request.GET.get("page")
            final = paginator.get_page(page_number)
            lastpage = final.paginator.num_pages

            return render(
                request, "temp/product_list_page.html", {"data": final, "lastpage": lastpage}
            )
    except Exception as e:
        print("something went wrong")
        save_exception_to_database(request.user.id, "40", type(e), str(e), ip_address)

        return render(request, "temp/product_list_page.html")
    
    
def soft_delete(request, pk):
    try:
        queryset = Product.objects.get(id=pk)
        queryset.is_delete=True
        queryset.save()
        scheduled_time = datetime.now() + timedelta(hours=1)
        permanent_delete_product.apply_async(eta=scheduled_time)
        messages.success(request, "Product has been deleted successfully")
        user_id_instence = User.objects.get(id=request.user.id)
        description = {
            "messages": "This user try to delete product",
            "data": request.POST,
        }
        activity = UserActivity(
            user_id=user_id_instence,
            IP=ip_address,
            description=f"this is username {request.user.username} and {description}",
        )
        activity.save()

        return redirect("product_list_page")

    except Exception as e:
        print("something went wrong")
        save_exception_to_database(request.user.id, "40", type(e), str(e), ip_address)



