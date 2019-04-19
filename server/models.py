from django.db import models


class TempModel(models.Model):
    temp = models.FloatField()
    datetime_stamp = models.DateTimeField()
    room = models.ForeignKey(
        'RoomModel',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        if self.room is None:
            return "Null, " + str(self.temp)
        return self.room.name + ", " + str(self.temp)


class RoomModel(models.Model):
    temps = models.ForeignKey(
        'TempModel',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

