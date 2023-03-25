from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date
import uuid
from django.contrib import admin

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Service(models.Model):
    SERVICE_TYPE_CHOICES = (
        ('photo', 'Photography'),
        ('video', 'Videography'),
        ('decor', 'Decoration'),
        ('catering', 'Catering'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=122)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    header = models.CharField(max_length=122)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=255, default='', blank=True)
    state = models.CharField(max_length=255, default='')
    featured_package_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    organizer = models.CharField(max_length=122, default='')
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class WeddingBooking(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)
    featured_package_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f'{self.service.title} booking for {self.customer.name} on {self.date_booked}'

