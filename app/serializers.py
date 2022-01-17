from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models, transaction
from .models import *
from cloudinary.models import CloudinaryField

from django.contrib.auth import get_user_model
from django.db import models, transaction
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import filters


# User Serializer
User = get_user_model()
# User Serializer
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        many=True
        model = User
        fields =  ['id','username','email','phone','role','password']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], phone = self.data.get('phone'),role = self.data.get('role'))
    
        return user   

'''
    registration serializer class
'''
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['id','username','email','phone','password','role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], phone = self.data.get('phone'),role = self.data.get('role'))
        return user

class ProfileSerializer(serializers.ModelSerializer):
    profile_pic = CloudinaryField('image')
    class Meta:
        model = Profile
        fields = ('user','name','location','bio','profile_pic')
'''
    admin's info serializer class
'''
class AdminInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminInput
        fields = ('id','name','status','recomendations','remarks')

'''
    customer's info serializer class
'''
class CustomerInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInput
        fields = ('id','user','name','phonenumber','location')

''' 
    referal serializer class
'''
class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = ('user','id','name','contact','location')         

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields =  ('id','user','name','phonenumber','types','bundle','location')