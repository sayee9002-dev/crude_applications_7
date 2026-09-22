from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    event_date = models.DateField()
    organizer = models.CharField(max_length=255)
    ticket_price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        self.event_name

