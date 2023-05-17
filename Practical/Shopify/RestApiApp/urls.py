from django.urls import path
from .import views
urlpatterns = [

    path('productlist/',views.ProductListApiView.as_view(),name='productlist'),
    path('productcreate/',views.ProductCreateApiView.as_view(),name='productcreate'),
    path('productupdate/<int:pk>',views.ProductupdateApiView.as_view(),name='productupdate'),
    path('productdelete/<int:pk>',views.ProductdeleteApiView.as_view(),name='productdelete'),
    path('productretrive/<int:pk>',views.ProductretriveApiView.as_view(),name='productretrive'),

    path('productapi/',views.Productlistcreteview.as_view(),name='productlistcreate'),
    path('productapi/<int:pk>',views.Productretriveupdatedeleteview.as_view(),name='productlistretriveupdatedelete'),

    path('productgetlist/',views.ProductApiView.as_view(),name='productgetlist'),
    path('productgetlist/<int:pk>',views.ProductChange.as_view(),name='productchange'),

    path('exportcsv/',views.ImportExcel.as_view(),name='exportcsv'),

]
