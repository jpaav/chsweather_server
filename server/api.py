from rest_framework import generics, authentication, permissions

from .serializers import *


class TempView(generics.RetrieveAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = TempSerializer

    def get_queryset(self):
        return TempModel.objects.all()

    def get_object(self):
        temp_id = self.kwargs.get('temp_id')
        return TempModel.objects.get(pk=temp_id)


class TempCreateView(generics.CreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = ()
    # permission_classes = ()

    serializer_class = TempSerializer

    def perform_create(self, serializer):
        temperature = serializer.save()


class RoomView(generics.RetrieveAPIView):
    lookup_field = 'room_id'
    authentication_classes = ()
    permission_classes = ()
    serializer_class = RoomDetailSerializer

    def get_queryset(self):
        return RoomModel.objects.all()

    def get_object(self):
        room_id = self.kwargs.get('room_id')
        return RoomModel.objects.get(pk=room_id)


class RoomListView(generics.ListAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = RoomModel.objects.all()
    serializer_class = RoomSerializer
