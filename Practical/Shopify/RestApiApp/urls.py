from django.urls import path
from .import views
urlpatterns = [
    path('productgetlist/<int:pk>',views.ProductChange.as_view(),name='productchange'),
    path("ProductApiViewwithCRUD",views.ProductApiViewwithCRUD.as_view(),name="ProductApiViewwithCRUD"),
    path("ProductApiViewwithCRUD/<int:pk>",views.ProductApiViewwithCRUD.as_view(),name="ProductApiViewwithCRUD")

]
