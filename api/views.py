from rest_framework import viewsets
from myapp.models import Product,ProductImage
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.

# class productlistViewset(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
# class productImagelistViewset(viewsets.ModelViewSet):
#     queryset = ProductImage.objects.all()
#     serializer_class = ProductImageSerializer


class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
    
        
