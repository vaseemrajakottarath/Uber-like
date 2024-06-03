from rest_framework import serializers
from . models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('id','username','is_driver','is_passenger')

class driverSerializer(serializers.ModelSerializer):
    class Meta :
        model = driver
        
        fields = ('id','user','approved')

class passengerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = passenger
        fields = ('id', 'user')
