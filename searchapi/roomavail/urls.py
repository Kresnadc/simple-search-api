from django.urls import path
from . import views

app_name = 'roomavail'

urlpatterns = [
    path('', views.avail_number, name='avail_number'),
]