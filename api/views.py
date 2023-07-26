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

# from django.shortcuts import render
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from .serializer import UserSerializer
# from .models import User


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         queryset = super().get_queryset()

#         age_param = self.request.query_params.get('age')
#         email_param = self.request.query_params.get('email')
#         phone_number_param = self.request.query_params.get('phone_number')

#         if age_param:
#             try:
#                 age_value = int(age_param)
#                 queryset = queryset.filter(age=age_value)
#             except ValueError:
#                 return Response(
#                     {"message": "El parámetro 'age' debe ser un número entero."},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#         if email_param:
#             queryset = queryset.filter(email=email_param)

#         if phone_number_param:
#             queryset = queryset.filter(phone_number=phone_number_param)

#         if not age_param and not email_param and not phone_number_param:
#             return Response(
#                 {"message": "Debes proporcionar al menos uno de los siguientes parámetros: 'age', 'email', 'phone_number'."},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         if not queryset.exists():
#             return Response(status=status.HTTP_200_OK)

#         return queryset
