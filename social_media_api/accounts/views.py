from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model

from .serializers import RegisterSerializer, LoginSerializer, UserMiniSerializer

User = get_user_model()


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

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if target_user == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(target_user)
        return Response({"detail": f"You are now following {target_user.username}."}, status=status.HTTP_200_OK)


class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if target_user == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(target_user)
        return Response({"detail": f"you have unfollowed {target_user.username}."}, status=status.HTTP_200_OK)


