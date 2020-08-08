from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation, Room

# Create your views here.
def room_avail(request):
    # persons = Person.objects.all().order_by('first_name')
    room = Room.objects.filter(room_status='available')

    reservation = Reservation.objects.filter(pub_date__gte=datetime.date(2020, 8, 8))

    return render(request, 'roomavail/room_avail.html', {'room': room})