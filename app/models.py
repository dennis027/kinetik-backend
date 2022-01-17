
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField
from datetime import date, datetime as dt
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
# Create your models here.

class User(AbstractUser):
    role_choices = (('is_admin','Admin'),('is_customer','Customer'))
    role = models.CharField(max_length=20, choices=role_choices,null=False)
    phone = models.IntegerField(blank=False,default=0) 


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True),
    def __str__(self):
        return self.user.username

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True),
    def __str__(self):
        return self.user.username


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True),
    def __str__(self):
        return self.user.username

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True),
    def __str__(self):
        return self.user.username
'''
    referal table for customers
'''
class Referral(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, blank=True)
    contact = models.IntegerField(blank=False,unique=True)
    location = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f'{self.user.username}'

'''
    profile model to all user
'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=255, default="Add Bio....", blank=True)
    name = models.CharField(max_length=60,blank=True)
    location = models.CharField(max_length=60,blank=True)
    contact = models.ManyToManyField(Referral)
    profile_pic= CloudinaryField('image' , default="Customer")

    def __str__(self):
        return f'{self.user.username} profile'


'''
    customer info table model
'''
class CustomerInput(models.Model):  
    '''
    pass
    '''
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')    
    # name = models.CharField(max_length=300,blank=True)
    # phonenumber = models.IntegerField(blank=True)
    # location = models.CharField(max_length=300,blank=True,default='location')
    # # date_modified = models.DateField(auto_now=True,)

    # def __str__(self):
    #     return f'{self.user.username} patient'
'''
    admin info table model
'''
class AdminInput(models.Model):
    response=(
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),   
    )
    recomend=(
        ('wait we will give feedback on installation','Wait we will give feedback on installation'),
        ('sorry our services are not available now', 'Sorry our services are not available now'),   
    )
    name = models.CharField(max_length=60,blank=True)
    status = models.CharField(choices=response,blank=False,default=0,max_length=200)
    recomendations = models.CharField(choices=recomend,blank=False,default=0,max_length=1000)
    remarks = models.TextField(max_length=1000,blank=True)
   
class Customer(models.Model):
    typ=(
        ('home','Home'),
        ('business','Business')
    )
    bund=(
        ('bronze','Bronze'),
        ('silver','Silver'),
        ('gold','Gold'),
        ('diamond','Diamond')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')    
    name = models.CharField(max_length=300,blank=True)
    phonenumber = models.IntegerField(blank=True,default=0) 
    types= models.CharField(choices=typ,blank=False,default=0,max_length=200)
    bundle=models.CharField(choices=bund,blank=False,default=0,max_length=200)
    location = models.CharField(max_length=300,blank=True,default='location')