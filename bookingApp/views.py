from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from django.views import View

from .forms import BookingForm
from .models import Service, Customer, WeddingBooking, Feedback, ContactForm, ContactNumber


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
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.service_id = service_id
            booking.featured_package_price = service.featured_package_price
            booking.save()
            messages.success(request, 'Booking has been created!')
            return redirect(reverse('booking_detail', args=(booking.id,)))
    return render(request, 'booking_form.html',{'form':form,'service':service})
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     phone = request.POST['phone']
    #     # address = request.POST['address']
    #     # country = request.POST['country'] address=address, country=country
    #     customer = Customer(name=name, email=email, phone=phone,)
    #     customer.save()
    #     booking = WeddingBooking(service=service, customer=customer, featured_package_price=service.featured_package_price)
    #     booking.save()
    #     messages.success(request, 'Booking has been created!')
    #     return redirect(reverse('booking_detail', args=(booking.id,)))


def bookings(request):
    bookings = WeddingBooking.objects.all()
    return render(request, 'bookings.html', {'bookings': bookings})

def booking_detail(request, booking_id):
    # booking = get_object_or_404(WeddingBooking, id=booking_id) {'booking': booking}
    return render(request, 'booking_detail.html')

def pay_booking(request, booking_id):
    booking = get_object_or_404(WeddingBooking, id=booking_id)
    if request.method == 'POST':
        booking.payment_status = 'paid'
        booking.save()
        messages.success(request, 'Payment has been received!')
        return redirect(reverse('booking_detail', args=(booking.id,)))
    return render(request, 'pay_booking.html', {'booking': booking})

class About(View):
    def get(self,request):
        return render(request, 'about.html')

class Profile(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return render(request, 'profile.html')
        else:
            return redirect('login')


class Contact(View):
    def get(self, request):
        contact = ContactNumber.objects.all()
        return render(request, 'contact.html', {'contact': contact})

    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        if name == '' or email == '' or message == '':
            messages.warning(request, 'Please fillup all the fields to send message!')
            return redirect('contact')

        else:
            form = ContactForm(name=name, email=email, message=message)
            form.save()
            messages.success(request, 'You have successfully sent the message!')
            return redirect('contact')


class Feedbacks(View):
    def get(self, request):
        feedback = Feedback.objects.all().order_by('-id')
        return render(request, 'feedback.html', {'feedback': feedback})

    def post(self, request):
        user = request.user
        if user.is_authenticated:
            comment = request.POST['feedback']

            if comment == '':
                messages.warning(request, "please write something first and then submit feedback.")
                return redirect('feedback')

            else:
                feedback = Feedback(name=user.first_name + ' ' + user.last_name, feedback=comment)
                feedback.save()
                messages.success(request, 'Thanks for your feedback!')
                return redirect('feedback')

        else:
            messages.warning(request, "Please login first to post feedback.")
            return redirect('feedback')