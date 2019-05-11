
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


class TempSerializer(serializers.ModelSerializer):
    temp = serializers.FloatField()
    room_name = serializers.CharField(source='room.name')
    room_pk = serializers.IntegerField(source='room.pk')
    datetime_stamp = serializers.DateTimeField()

    class Meta:
        model = TempModel
        fields = (
            'pk',
            'temp',
            'room_name',
            'room_pk',
            'datetime_stamp',
        )
        read_only_fields = (
            'pk',
        )


class RoomDetailSerializer(serializers.ModelSerializer):
    temps = TempSerializer(many=True)
    name = serializers.CharField()
    department = serializers.CharField()

    class Meta:
        model = RoomModel
        fields = (
            'pk',
            'temps',
            'name',
            'department'
        )
        read_only_fields = (
            'pk',
        )


class RoomSerializer(serializers.ModelSerializer):
    temp = TempSerializer(source='get_first_temp')
    name = serializers.CharField()
    department = serializers.CharField()

    class Meta:
        model = RoomModel
        fields = (
            'pk',
            'temp',
            'name',
            'department'
        )
        read_only_fields = (
            'pk',
        )
