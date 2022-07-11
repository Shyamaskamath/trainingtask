from email.policy import default
from rest_framework import serializers
from user.models import CustomUser
from myapp.models import ProductImage,Product
from django.contrib.auth.models import Group
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""
    email=serializers.EmailField(required=True, 
	validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password=serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
    password2=serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields = ('email','password', 'password2')
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
             raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            )
        user.set_password(validated_data['password'])
        mygroup=Group.objects.get(name='customer')
        mygroup.user_set.add(user)
        user.save()
        return user


class LoginSeralizer(serializers.Serializer):
    """ seralizer for user login with email and password"""
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128)

class ProductImageSeralizer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = ProductImage
        fields = ('id','image')
    
class ProductSeralizer(serializers.ModelSerializer):
    """seralizer for Product model """ 
    images = ProductImageSeralizer(many=True,read_only=True)
    class Meta:
        model = Product
        fields = ('id','title','itemno','description','images')


    def create(self, validated_data):
        imagedata =self.context.get('view').request.FILES
        product=Product.objects.create(title=validated_data.get('title', 'no-title'),
        itemno=validated_data.get('itemno', 'no-itemno'),
        description=validated_data.get('description', 'no-description'))
        for imagedata in imagedata.values():
            ProductImage.objects.create(product=product,image=imagedata)
        return product

class ProfileUpdateSeralizer(serializers.ModelSerializer):
    """seralizer for profile update"""
    email = serializers.EmailField(required=True, 
	validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email','mobile','profile_photo')
    
    







