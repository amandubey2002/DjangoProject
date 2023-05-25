from frontapp.models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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


class ProductApiViewwithCRUD(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self,request,pk=None,*args, **kwargs):
        
        if pk:
            queryset = Product.objects.filter(id=pk).first()
            print(queryset)
            
            if queryset:
                serializer = ProductSerializer(queryset)
                return Response(serializer.data)
            
            else:
                return Response({"msg":"No data found"})
            
        else:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset,many=True)
            return Response(serializer.data)
    

    def post(self, request,*args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,*args, **kwargs):
        queryset = Product.objects.filter(id=pk).first()
        print(queryset)
        if queryset:
            serializer = ProductSerializer(queryset,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"not updated sucsessfully"})

    def delete(self,request,pk=None):
        queryset = Product.objects.get(id=pk)
        print(queryset)
        if queryset:
            queryset.delete()
            return Response({"msg":"sucsessfully deleted"})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)