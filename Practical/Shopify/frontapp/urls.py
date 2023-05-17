from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("registration/", views.signup, name="registration"),
    path("change_password/", views.change_password, name="change_password"),
    path(
        "change_password/<token>",
        views.change_password_with_token,
        name="change_password",
    ),
    path("forgot-password/", views.forgot_password_with_email, name="forgot-password"),
    path("export_pdf/", views.import_pdf, name="export_pdf"),
    path("product_list/", views.ProductListApiView.as_view(), name="product_list"),
    path("csv_import/", views.import_csv_with_thread, name="csv_import"),
    path("export_csv/", views.export_csv, name="export_csv"),
    path("export_csv1/", views.export_csv1, name="export_csv1"),
    path("data_to_pdf/", views.generate_pdf, name="data_to_pdf"),
    path("productlist1/", views.ProductList, name="productlist1"),
    path("product_delete/<int:pk>", views.delete_product, name="product_delete"),
    path("home/", views.delete_multiple_product, name="home"),
    path("send_mail/", views.send_mail_to_all_users, name="send_mail"),
    path("productwithuserview/", views.create_product, name="productwithuserview"),
]
