from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from api.v1.user.serializers import LoginSerializer

User = get_user_model()


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = self.request.data.get('username', '')
        password = self.request.data.get('password', '')
        if not username:
            if not password:
                return Response(dict(username='Required field.', password='This field cannot be empty.'),
                                status=status.HTTP_400_BAD_REQUEST)
            return Response(dict(username='Required field.'), status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response(dict(password='This field cannot be empty.'), status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(username=username)
        if not user.exists():
            return Response(
                {'detail': f'The username you entered isn’t connected to an account'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        if not user.first().check_password(password):
            return Response({'detail': 'You entered an incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = LoginSerializer(user.first())
        return Response(serializer.data)
