from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.authtoken.models import Token
from rest_framework import generics

from django.contrib.auth import get_user_model

from .serializers import RegisterSerializer, LoginSerializer, UserMiniSerializer

CustomUser = get_user_model()

class RegisterView(APIView):
    """
    POST /api/accounts/register
    Registers a new user and returns { user, token } on success.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # Token created inside serializer
        token = Token.objects.get(user=user)  # retrieve token created
        return Response(
            {
                "user": UserMiniSerializer(user, context={"request": request}).data,
                "token": token.key,
            },
            status=status.HTTP_201_CREATED,
        )


class LoginView(APIView):
    """
    POST /api/accounts/login
    Authenticates a user and returns { user, token }.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                "user": UserMiniSerializer(user, context={"request": request}).data,
                "token": token.key,
            },
            status=status.HTTP_200_OK,
        )


class ProfileView(RetrieveUpdateAPIView):
    """
    GET /api/accounts/profile
    PUT/PATCH /api/accounts/profile
    View & update the authenticated user profile.
    """
    serializer_class = UserMiniSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser.objects.all(), id=user_id)
        request.user.following.add(user_to_follow)
        return Response({"detail": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser.objects.all(), id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"detail": f"You unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)

