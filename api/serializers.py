from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from myapp.models import Product,ProductImage
from user.models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group

# class ProductSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Product
# 		fields = ('id','title','itemno','description')
	
# class ProductImageSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = ProductImage
# 		fields = ('id','product','image')

# class UserSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = CustomUser
#     fields = ["id", "username","email"]

class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=CustomUser.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = CustomUser
    fields = ('username', 'password', 'password2',
         'email')
    
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
  def create(self, validated_data):
	
    user = CustomUser.objects.create(
    username=validated_data['username'],
    email=validated_data['email'],

    )
    user.set_password(validated_data['password']);mygroup = Group.objects.get(name='customer');mygroup.user_set.add(user)
    user.save();Token.objects.get_or_create(user=user);return user

