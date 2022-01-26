from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from api.v1.user.serializers import LoginSerializer
from api.v1.user.validate import validate_user

User = get_user_model()


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = self.request.data.get('username', '')
        password = self.request.data.get('password', '')
        user = validate_user(username=username, password=password)
        if isinstance(user, Response):
            return user
        serializer = LoginSerializer(user.first())
        return Response(serializer.data)
