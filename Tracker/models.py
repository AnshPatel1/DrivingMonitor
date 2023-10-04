from django.db import models


# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=1024)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.active}"

    class Meta:
        verbose_name_plural = "Organizations"
        verbose_name = "Organization"


class TrackerNode(models.Model):
    is_online = models.BooleanField(default=False)
    group = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return f"Tracker Node of {self.group.name} | Online Status: {self.is_online}"

    class Meta:
        verbose_name_plural = "Tracker Nodes"
        verbose_name = "Tracker Node"


class Trip(models.Model):
    node = models.ForeignKey(TrackerNode, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.node} | Start {self.start_time} | End: {self.end_time}"

    class Meta:
        verbose_name_plural = "Trips"
        verbose_name = "Trip"


class LocationHistory(models.Model):
    models.ForeignKey(Trip, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=50, decimal_places=24)
    longitude = models.DecimalField(max_digits=50, decimal_places=24)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{str(self.latitude)}, {str(self.longitude)} | {self.timestamp}"

    class Meta:
        verbose_name_plural = "Location History Timeline"
        verbose_name = "Location History"
