from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from .models import Service, Customer, WeddingBooking

def index(request):
    services = Service.objects.all()
    return render(request, 'index.html', {'services': services})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'service_detail.html', {'service': service})

def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, 'customer_detail.html', {'customer': customer})

def book_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        country = request.POST['country']
        customer = Customer(name=name, email=email, phone=phone, address=address, country=country)
        customer.save()
        booking = WeddingBooking(service=service, customer=customer, featured_package_price=service.featured_package_price)
        booking.save()
        messages.success(request, 'Booking has been created!')
        return redirect(reverse('booking_detail', args=(booking.id,)))
    return render(request, 'book_service.html', {'service': service})

def bookings(request):
    bookings = WeddingBooking.objects.all()
    return render(request, 'bookings.html', {'bookings': bookings})

def booking_detail(request, booking_id):
    booking = get_object_or_404(WeddingBooking, id=booking_id)
    return render(request, 'booking_detail.html', {'booking': booking})

def pay_booking(request, booking_id):
    booking = get_object_or_404(WeddingBooking, id=booking_id)
    if request.method == 'POST':
        booking.payment_status = 'paid'
        booking.save()
        messages.success(request, 'Payment has been received!')
        return redirect(reverse('booking_detail', args=(booking.id,)))
    return render(request, 'pay_booking.html', {'booking': booking})
