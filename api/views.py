# # from django.shortcuts import render
# from rest_framework import viewsets
# from .serializer import UserSerializer
# from .models import User

# # Create your views here.

# class UserViewSet(viewsets.ModelViewSet):
#   queryset = User.objects.all()[:2]
#   serializer_class = UserSerializer


from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.query_params.get('age'):
            queryset = queryset.filter(age=self.request.query_params.get('age'))

        if self.request.query_params.get('email'):
            queryset = queryset.filter(email=self.request.query_params.get('email'))

        if self.request.query_params.get('phone_number'):
            queryset = queryset.filter(phone_number=self.request.query_params.get('phone_number'))

        return queryset
