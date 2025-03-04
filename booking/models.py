from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField(blank=True)
    demo_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.demo_date}"

# Create your models here.
