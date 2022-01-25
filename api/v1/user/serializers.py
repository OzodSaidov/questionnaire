from rest_framework import serializers

from user.token import MyTokenObtainPairSerializer


class LoginSerializer(serializers.Serializer):
    def to_representation(self, instance):
        data = super(LoginSerializer, self).to_representation(instance)
        refresh_token = MyTokenObtainPairSerializer.get_token(instance)
        access_token = refresh_token.access_token
        data['access_token'] = str(access_token)
        data['refresh_token'] = str(refresh_token)
        return data
