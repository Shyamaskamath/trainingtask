from rest_framework.viewsets import ModelViewSet
from myapp.models import Product
from rest_framework.views import APIView
from user.models import CustomUser
from django.shortcuts import get_object_or_404
from .serializers import RegisterSerializer,LoginSeralizer,PasswordChangeSeralizer,ProductSeralizer,ProductImageSeralizer,ProfileUpdateSeralizer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework import status,generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

class RegistrationAPIView(generics.CreateAPIView):
  """view for user registration """
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
    
class LoginAPIView(APIView):
    """view for login with email and password """
    permission_classes = (AllowAny,)
    serializer_class = LoginSeralizer

    def post(self, request, *args, **kwargs):
        """overrides post method """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.data['email']
            password = serializer.data['password']
            user = authenticate(email=email, password=password)
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

class ProductListAPIView(GenericAPIView,ListModelMixin):
    """endpoint for product list """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = ProductSeralizer
    queryset = Product.objects.all()
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class ProductDetailAPIView(GenericAPIView,RetrieveModelMixin):
    """endpoint for detailed view of a product"""
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = ProductSeralizer
    queryset = Product.objects.all()
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class ProductUpdateAPIView(GenericAPIView,UpdateModelMixin):
    """endpoint to update the productdetails(itemno,description,title) """
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]
    serializer_class = ProductSeralizer
    queryset = Product.objects.all()
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class ProductDeleteAPIView(GenericAPIView,DestroyModelMixin):
    """endpoint to deleteproduct"""
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Product.objects.all()
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class CreateViewset(ModelViewSet):
    """endpoint to create new products """
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]
    serializer_class = ProductSeralizer
    queryset= Product.objects.all()

class ProfileUpdateAPIView(generics.RetrieveUpdateAPIView):
    """endpoint to update user profile"""
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = ProfileUpdateSeralizer
    def get_object(self):
        return get_object_or_404(CustomUser, id=self.request.user.id)
    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)






   





    




    
    
    




    












       
        
