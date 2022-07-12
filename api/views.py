from rest_framework.viewsets import ModelViewSet
from myapp.models import Product, ProductImage
from rest_framework.views import APIView
from user.models import CustomUser
from django.shortcuts import get_object_or_404
from .serializers import RegisterSerializer,LoginSeralizer,ProductSeralizer,ProfileUpdateSeralizer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework import status,generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistrationAPI(generics.CreateAPIView):
  """endpoint for user registration """
  permission_classes=(AllowAny,)
  serializer_class=RegisterSerializer
    
class LoginAPI(APIView):
    """endpoint for login with email and password """
    permission_classes=(AllowAny,)
    serializer_class=LoginSeralizer

    def post(self, request, *args, **kwargs):
        """overrides post method """
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            email=serializer.data['email']
            password=serializer.data['password']
            user=authenticate(email=email, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({'status':200,'payload':serializer.data,'refresh': str(refresh),
                 'access': str(refresh.access_token),})
            else:
                content = {'detail':('Unable to login with provided credentials.')}
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

class ProductListAPI(GenericAPIView,ListModelMixin):
    """endpoint to list all product """
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    serializer_class=ProductSeralizer
    queryset=Product.objects.all()
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class DetailProductListAPI(GenericAPIView,RetrieveModelMixin):
    """endpoint for detailed view of a product"""
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    serializer_class=ProductSeralizer
    queryset=Product.objects.all()
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class ProductListCreateAPI(ModelViewSet):
    """endpoint to create new products and view product"""
    permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [JWTAuthentication]
    serializer_class = ProductSeralizer
    queryset= Product.objects.all()

class RetriveUpdateDeleteProductAPI(generics.RetrieveUpdateDestroyAPIView): 
    """endpoint to  retrive, update and delete product details""" 
    permission_classes=[IsAuthenticated,IsAdminUser] 
    authentication_classes=[JWTAuthentication] 
    serializer_class=ProductSeralizer 
    queryset= Product.objects.all() 
    def get_queryset(self):
        """overrides get method"""
        try:
            Productobject = Product.objects.filter(id=self.kwargs['pk'])
            return Productobject
        except Productobject.DoesNotExist:
            return JsonResponse({"error": "Product Doesnt exist"},
                                status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, *args, **kwargs): 
        """ to ovverride the updae method"""
        productid=self.kwargs['pk']
        productobject=Product.objects.get(id=productid)
        list_deleting_ids=request.data['list'].split(',')
        ProductImage.objects.filter(id__in=list_deleting_ids, product=productobject).delete()
        imagess = request.data.get('image')
        if imagess: 
            image = request.data.pop('image')
            ProductImage.objects.bulk_create([ProductImage(product=productobject,image=imagedata)  
            for imagedata in image ]) 
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        """ override the delete method """
        productid=self.kwargs['pk']
        try:
            productobject=Product.objects.get(id=productid)
            productobject.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product Doesnt exist"},
                                status=status.HTTP_400_BAD_REQUEST)
     
class ProfileUpdateAPI(generics.RetrieveUpdateAPIView):
    """endpoint to update user profile"""
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    serializer_class=ProfileUpdateSeralizer
    def get_object(self):
        return get_object_or_404(CustomUser, id=self.request.user.id)
    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)





   





    




    
    
    




    












       
        