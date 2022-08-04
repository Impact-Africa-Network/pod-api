from ian_account.models import User
from rest_framework import serializers


class UserTokenSerializer(serializers.ModelSerializer):
    """Generate User Token Serializer"""
    class Meta:
        model = User
        fields = ["id", "status", "is_active", "email", "is_staff"]
class UserDetailSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = User
        fields = [ 
            "id",
            "email",
            "first_name",
            "last_name",
            "token",
        ]


class UserSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    password = serializers.CharField(min_length=8, max_length=64)

    

class UserSignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()