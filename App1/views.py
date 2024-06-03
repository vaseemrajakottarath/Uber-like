from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from . models import *
from . serializers import *
from rest_framework.response import Response

# Create your views here.

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self,request,*args,**kwrgs):
        user_type = request.data.get('user_type')

        if user_type not in ['admin','driver','passenger']:
            return Response({"error":"invalid user"},status= status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(
            username = request.data.get('username'),
            password=request.data.get('password'),
            is_staff=(user_type == 'admin'),
            is_superuser=(user_type == 'admin'),
            is_driver=(user_type == 'driver'),
            is_passenger=(user_type == 'passenger'),
        )
        user.save()
        
        if user_type == 'driver':
            driver.objects.create(user = user)
        elif user_type == 'passenger':
            passenger.objects.create(user = user)
        
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data}
        ,status=status.HTTP_201_CREATED)

class DriverViewSet(viewsets.ModelViewSet):
    queryset = driver.objects.all()
    serializer_class = driverSerializer

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def approve(self, request, pk=None):
        driver = self.get_object()
        driver.approved = True
        driver.save()
        return Response({'status': 'Driver approved'})