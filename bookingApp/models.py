from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date
import uuid
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=122, default='test')
    email_id = models.EmailField(default='xx@xx.com')
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255,blank=True,null=True)

    class Meta:
        verbose_name = "Customers"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name


class Service(models.Model):
    SERVICE_TYPE_CHOICES = (
        ('photo', 'Photography'),
        ('video', 'Videography'),
        ('decor', 'Decoration'),
        ('catering', 'Catering'),
        ('music', 'Music DJ'),
        ('makeup', 'Makeup'),
        ('wedding_planner', 'Wedding Planner'),
        ('resort', 'Resort')

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
    Currency_CHOICES = (
        ('CAD', 'CAD'),
        ('USD', 'USD'),
        ('INR','INR')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(max_length=122)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_booked = models.DateField()
    location = models.CharField(max_length=200)
    featured_package_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    payment_currency = models.CharField(max_length=10, choices=Currency_CHOICES, default='CAD')

    def __str__(self):
        return f'{self.service.title} Booking in the name of {self.name}'

class Feedback(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=255, null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class ContactForm(models.Model):
    name = models.CharField(verbose_name=_("Sender Name"), max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'Sender {self.name} has a message for you'

class ContactNumber(models.Model):
    phone = models.CharField(verbose_name=_("Station Phone Number"), max_length=255, null=True, blank=True)
    emergency_center = models.CharField(verbose_name=_("Emergency Center Phone Number"), max_length=255, null=True,
                                        blank=True)
    help_desk = models.CharField(verbose_name=_("Help Desk Phone Number"), max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
