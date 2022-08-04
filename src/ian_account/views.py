import email
from django.contrib.auth import get_user_model
from django.shortcuts import render
from ian_auth import permissions
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from . import serializers as sz

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    Sign Up

    Sign In
    """

    permission_classes = (permissions.AllowAny,)
    serializer_class = sz.UserDetailSerializer
    queryset = User.objects.all().exclude(is_superuser=True)
    # filter_backends = [DjangoFilterBackend, SearchFilter]
    # filterset_class = ft.UserFilter

    def get_serializer_class(self):
        if self.action == "list":
            return None
        return sz.UserDetailSerializer

    @action(
        methods=["POST"],
        detail=False,
        permission_classes=[permissions.AllowAny],
        url_path="signup",
    )
    def signup(self, request: Request) -> Response:
        """Signs up a new user

        Args:
            request (Request): _description_

        Returns:
            response (Response): the response object. Includes a msg, success status, status code, and the user object.
        """
        serializer = sz.UserSignUpSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "error": True,
                    "data": serializer.errors,
                    "msg": "Invalid data",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = serializer.data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        password = data.get("password")

        try:
            user, created = User.objects.get_or_create(
                email=email,
                defaults={
                    "first_name": first_name,
                    "last_name": last_name,
                },
            )
        except Exception as e:
            print(e)
            return Response(
                {
                    "error": True,
                    "data": None,
                    "msg": "Something wrong happened. Try again later",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        if not created:
            return Response(
                {
                    "error": True,
                    "data": None,
                    "msg": "Looks like you already have an account, sign in instead?",
                },
                status=status.HTTP_409_CONFLICT,
            )
        user.set_password(password)
        user.is_active = True
        user.token = user.generate_token()
        user.save()

        response = sz.UserDetailSerializer(user)

        return Response(
            {"success": True, "data": response.data, "msg": "Signed up successfully"},
            status=status.HTTP_201_CREATED,
        )


class UserAuthViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny,]
    serializer_class = sz.UserDetailSerializer
    queryset = User.objects.all().exclude(is_superuser=True)
    # filter_backends = [DjangoFilterBackend, SearchFilter]
    # filterset_class = ft.UserFilter

    @action(methods=["POST"], detail=False, permission_classes=[permissions.AllowAny], url_path="signin")
    def signin(self, request: Request) -> Response:
        """Signs user in

        Args:
            request (Request): _description_

        Returns:
            Response: _description_
        """
        serializer = sz.UserSignInSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "error": True,
                    "data": serializer.errors,
                    "msg": "Invalid data",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = serializer.data
        email = data.get("email")
        password = data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {
                    "error": True,
                    "data": None,
                    "msg": "User does not exist",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        if not user.check_password(password):
            return Response(
                {
                    "error": True,
                    "data": None,
                    "msg": "Invalid credentials",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        user.token = user.generate_token()
        user.save()
        user.refresh_from_db()
        response = sz.UserDetailSerializer(user).data
        response.update({"token": user.token})
        return Response({"success": True, "data": response, "msg": "Signed in successfully"}, status=status.HTTP_200_OK)