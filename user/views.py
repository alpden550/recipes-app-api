from rest_framework.generics import CreateAPIView

from user.serializers import UserSerializer


class CreateUserView(CreateAPIView):
    """"Create a new user"""
    serializer_class = UserSerializer
