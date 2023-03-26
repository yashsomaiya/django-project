
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "marriageBookingSystem.settings")
django.setup()

from datetime import datetime
from django.contrib.auth.models import User
from bookingApp.models import Customer, Service, WeddingBooking

# Create some customers
customer1 = Customer.objects.create(name='John Doe', email='johndoe@example.com', phone='1234567890', address='123 Main St', country='USA')
customer2 = Customer.objects.create(name='Jane Doe', email='janedoe@example.com', phone='0987654321', address='456 Park Ave', country='USA')

# Create some services
service1 = Service.objects.create(title='Photography Service 1', service_type='photo', header='Header 1', desc='Description 1', city='New York', state='NY', featured_package_price=2000.00, organizer='Organizer 1')
service2 = Service.objects.create(title='Videography Service 1', service_type='video', header='Header 2', desc='Description 2', city='Los Angeles', state='CA', featured_package_price=2500.00, organizer='Organizer 2')

# Create some wedding bookings
booking1 = WeddingBooking.objects.create(service=service1, customer=customer1, date_booked=datetime.now(), featured_package_price=2500.00, payment_status='pending')
booking2 = WeddingBooking.objects.create(service=service2, customer=customer2, date_booked=datetime.now(), featured_package_price=3000.00, payment_status='paid')
