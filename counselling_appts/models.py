from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Appointment(models.Model):
    '''appointment details'''

    APPOINTMENT_STATUS = (
        (0, "Pending confirmation"),
        (1, "Confirmed"),
        (2, "Canceled")
    )

    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='appointments'
    )
    date = models.DateTimeField()
    status = models.SmallIntegerField(choices=APPOINTMENT_STATUS, default=0)
    comment = models.TextField(default="", blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.date: %d %B %Y at %H:%M} - Client Name: {self.client}'


class Message(models.Model):
    '''Mesages to the counsellor'''

    MESSAGE_STATUS = (
        (0, "Unread"),
        (1, "Read"),
        (2, "Replied")
    )

    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='messages'
    )
    text = models.TextField(blank=False, default="")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.SmallIntegerField(choices=MESSAGE_STATUS, default=0)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.date: %d %B %Y at %H:%M} - Client Name: {self.client}'
