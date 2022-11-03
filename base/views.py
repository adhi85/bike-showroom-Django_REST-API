from django.shortcuts import render
from .models import bikes,Category
# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer,bikesSerializer,CategorySerializer
from django.contrib.auth import login

from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

# Register API

@api_view(['GET'])
def Routes(request):
    routes = [
        'GET /api/',
        'All OPERATIONS',
        'login: login user',
        'register: register a user',
        
        
    ]
    return Response (routes)

def home(request):
    return render(request, 'base/home.html')

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

class bikesList(generics.ListCreateAPIView):
    serializer_class = bikesSerializer

    def get_queryset(self):
        queryset = bikes.objects.all()
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(bikeCategory = category)
        return queryset

class bikesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = bikesSerializer
    queryset = bikes.objects.all()
    

class categoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class categoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()