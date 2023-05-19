from django.urls import path
from .import views


urlpatterns = [
    path("export_pdf/", views.import_pdf, name="export_pdf"),
    path("csv_import/", views.import_csv_with_thread, name="csv_import"),
    path("export_csv/", views.export_csv, name="export_csv"),
    path("export_csv1/", views.export_csv1, name="export_csv1"),
    path("data_to_pdf/", views.generate_pdf, name="data_to_pdf"),
    path("productlist1/", views.ProductList, name="productlist1"),
    path("product_delete/<int:pk>", views.delete_product, name="product_delete"),
    path("send_mail/", views.send_mail_to_all_users, name="send_mail"),
    path("productwithuserview/", views.create_product, name="productwithuserview"),
    path("product_list_page",views.product_list_page,name="product_list_page"),
    path("soft_delete/<int:pk>",views.soft_delete, name="soft_delete"),
]
