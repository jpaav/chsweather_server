from rest_framework import serializers

from .models import *


class TempSerializer(serializers.ModelSerializer):
    temp = serializers.FloatField()
    room_name = serializers.CharField(source='room.name', read_only=True)
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
            'room_name',
        )


class RoomDetailSerializer(serializers.ModelSerializer):
    temps = serializers.SerializerMethodField(read_only=True)
    name = serializers.CharField()
    department = serializers.CharField()

    def get_temps(self, obj):
        model_temps = list(TempModel.objects.filter(room=obj))
        serializer = TempSerializer(model_temps, many=True)
        return serializer.data

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
