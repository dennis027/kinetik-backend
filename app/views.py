from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import *
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets, generics,permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework import filters



# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

  

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

# Create your views here.

def index(request):
    return render (request, 'index.html')

    
class UserViewSet(viewsets.ModelViewSet):  
    search_fields = ['email','username']
    # filter_backends = (filters.SearchFilter)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

'''
     view set returning all CRUD and search method on profile model
'''
class ReferralViewSet(viewsets.ModelViewSet):
    search_fields = ['name','contact','user__username']
    filter_backends = (filters.SearchFilter,)
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer
'''
     view set returning all CRUD and search method on doctors input model
'''
class AdminInputViewSet(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = AdminInput.objects.all()
    serializer_class = AdminInputSerializer

'''
     view set returning all CRUD and search method on patient input model
'''
class CustomerInputViewSet(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = CustomerInput.objects.all()
    serializer_class = CustomerInputSerializer

'''
    view set returning all CRUD and search method on user model
'''
class UserViewSet(viewsets.ModelViewSet):
    search_fields = ['email','username']
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends=(filters.SearchFilter,)
    queryset=User.objects.all()
    serializer_class= CustomerSerializer



'''
    registration api view to post new users
'''

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "user_id": user.pk,
                "role": user.role,
                "email": user.email,
                "username": user.username,
            }
        )