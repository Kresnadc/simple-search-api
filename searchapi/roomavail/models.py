from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

class Room(models.Model):   
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.IntegerField(default=0)
    room_status = models.CharField(max_length=200)

class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    order_id = models.IntegerField(default=0)
    customer_name = models.CharField(max_length=200)
    checkin_date = models.DateTimeField('date checkin')
    checkout_date = models.DateTimeField('date checkout')

class Stay(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=200)

class StayRoom(models.Model):
    stay = models.ForeignKey(Stay, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateTimeField('date stay')