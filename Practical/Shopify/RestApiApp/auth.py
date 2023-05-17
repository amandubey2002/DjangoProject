from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class RegisterUserWithToken(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
        user = User.objects.get(username=serializer.data["username"])
        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                "status": status.HTTP_200_OK,
                "user_name": user.username,
                "email": user.email,
                "password": user.password,
                "token": token.key,
            }
        )
