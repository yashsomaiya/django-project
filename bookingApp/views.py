from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.views import View
from django.contrib.auth.models import User, auth
from .models import Service, Customer, WeddingBooking, Feedback, ContactForm, ContactNumber

def accountlogin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if username is not None and password is not None:
            if user is not None:
                auth.login(request, user)
                messages.info(request, "Successfully logged in!")
                return redirect('index')
            else:
                messages.info(request, "invalid credentials")
                return redirect('index')
    else:
        return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if username is not None and password is not None:
            if user is not None:
                auth.login(request, user)
                messages.info(request, "Successfully logged in!")
                return redirect('index')
            else:
                messages.info(request, "invalid credentials")
                return redirect('index')
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':  # fetching the data from form
        username = request.POST["username"]
        name = request.POST["name"]
        email = request.POST["email"]
        number = request.POST["number"]
        password = request.POST["password"]
        #   country = request.POST['country']
        print(username, name, email, number, password)
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already in use')
            return redirect('index')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username already in use')
            return redirect('index')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            cust = Customer.objects.create(name=name, phone=number, email_id=email)
            cust.save()
            messages.info(request, 'Successfully Registered. You can now login to your account.')
            return redirect('index')
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


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
        # address = request.POST['address']
        # country = request.POST['country'] address=address, country=country
        customer = Customer(name=name, email=email, phone=phone, )
        customer.save()
        booking = WeddingBooking(service=service, customer=customer,
                                 featured_package_price=service.featured_package_price)
        booking.save()
        messages.success(request, 'Booking has been created!')
        return redirect(reverse('booking_detail', args=(booking.id,)))
    return render(request, 'booking_form.html', {'service': service})


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
    def get(self, request):
        return render(request, 'about.html')


class Profile(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            try:
                customer = Customer.objects.get(email_id=user.email)
                phone_number = customer.phone
            except Customer.DoesNotExist:
                phone_number = None
            return render(request, 'profile.html', {'customer': customer})
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
