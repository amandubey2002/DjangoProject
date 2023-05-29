from django.urls import path
from .import views


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
    path("role_change/",views.Rolechange,name="role_change"),
    path("admin_dashboard/",views.admin_dashboard,name="admin_dashboard"),
    path("admin_login/",views.admin_login,name="admin_login"),
    path("delete_user/<int:pk>",views.user_delete,name="delete_user"),
    path("update_user/<int:pk>",views.update_user,name="update_user")
]