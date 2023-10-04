from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from DrivingMonitor import settings
from Tracker.views import dashboard, fleet

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('fleet/', fleet, name='fleet'),
]
