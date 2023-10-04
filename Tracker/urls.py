from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from DrivingMonitor import settings
from Tracker.views import dashboard, fleet, hawk_node, analysis

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('fleet/', fleet, name='fleet'),
    path('nodes/', hawk_node, name='nodes'),
    path('analysis/', analysis, name='analysis'),
]
