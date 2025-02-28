from django.db import models
from users.models import HouseOwner

class Room(models.Model):
    owner = models.ForeignKey(HouseOwner, on_delete=models.CASCADE, related_name="rooms")
    room_type = models.CharField(max_length=20, choices=[('single', 'Single'), ('family', 'Family')])
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=[('available', 'Available'), ('booked', 'Booked')])
    images = models.ImageField(upload_to='room_images/')
