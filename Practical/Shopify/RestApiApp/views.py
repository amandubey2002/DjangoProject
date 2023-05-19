from django.shortcuts import render
# from .models import 
from frontapp.models import Product
from .serializers import ProductSerializer
# Create your views here.
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class ProductListApiView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateApiView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductupdateApiView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductdeleteApiView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductretriveApiView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



#method 2nd



class Productlistcreteview(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Productretriveupdatedeleteview(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


#method 3rd



class ProductApiView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset,many=True)
        return Response(serializer.data)
    

    def post(self, request,*args,**kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    


class ProductChange(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


    def put(self,request,pk,*args,**kwargs):
        queryset = Product.objects.get(pk=pk)
        serializer = ProductSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        

    def delete(self,request,pk,*args,**kwargs):
        queryset = Product.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_200_OK)
