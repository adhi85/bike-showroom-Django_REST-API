from rest_framework import serializers
from django.contrib.auth.models import User
from .models import bikes, Category, Cart

# User Serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user

# category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class bikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = bikes
        fields = ('__all__')


class CartSerializer(serializers.ModelSerializer):

    cart_id = UserSerializer(read_only=True, many=False)
    bikes = bikesSerializer(read_only=True, many=False)

    class Meta:
        model = Cart
        fields = ('__all__')
