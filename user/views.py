from django.contrib.auth import logout
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, AuthTokenSerializer
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken


class RegisterView(generics.CreateAPIView):
    # Create a new user in the system
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class LoginView(ObtainAuthToken):
    # Create a new auth token for user
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class LogoutView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        logout(request)
        return Response('User logged out',
                        status=status.HTTP_204_NO_CONTENT)


class UserSelfView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_object(self):
        return self.request.user