from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()


def validate_user(username: str, password: str):
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

    return user
