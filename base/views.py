from django.shortcuts import render
from .models import bikes,Category,Cart
from django.contrib.auth.models import User
# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer,bikesSerializer,CategorySerializer,CartSerializer
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.decorators import permission_classes



# Register API

@api_view(['GET'])
@permission_classes((AllowAny, ))
def Routes(request):  
    routes = [
        'GET /api/',
        'All OPERATIONS',
        'api/auth/auth-token : Generate the token for the user '
        'api/login: login user',
        'api/register: register a user',
        'api/bikes: View all bikes and add bikes',
        'api/bikes/<str:pk>: View a specific bike and update its details',
        'api/category: View all the bike categories',
        'api/category/<str:pk>: View specific bike category and update it ',
        'api/carts: View all carts of all users and the bikes they purchased ',
        'api/carts/<str:pk>: View the cart of a specific user and purchase bikes.==> The bikes which the user has purchased ',
        
        

    ]
    return Response (routes)


def home(request):
    return render(request, 'base/home.html')

class RegisterAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
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
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = bikesSerializer

    def get_queryset(self):
        queryset = bikes.objects.all()
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(bikeCategory = category)
        return queryset

class bikesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = bikesSerializer
    queryset = bikes.objects.all()
    

class categoryList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class categoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

        
class ListCart(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer 




#OLD CODE

# @api_view(['GET'])
# def purchaseList(request):
#     bike = bikes.objects.all()
#     serializer = bikesSerializer(bike, many = True)

#     return Response(serializer.data)

# @api_view(['POST','GET'])
# def purchaseBike(request, pk):
#     bike = bikes.objects.get(id=pk)
#     # serializer = bikesSerializer(bike, many = False)
#     serializer = purchasedBikesSerializer(data = request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# class purchaseBike(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = purchasedBikesSerializer

#     queryset = purchasedBikes.objects.all()
#     def pur(self,queryset):
#         queryset.purchased_by = self.request.user