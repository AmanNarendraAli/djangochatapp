from django.db import models

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=255)

    def __str(self):
        return self.room_name

class Message(models.Model):
    room = models.ForeignKey(Room,related_name='messages',on_delete=models.CASCADE) #related_name allows us to access messages from a room instance using room.messages
    sender = models.CharField(max_length=255)
    content = models.TextField()

    def __str(self):
        return f'{self.sender} IN {self.room}: {self.content[:20]}'