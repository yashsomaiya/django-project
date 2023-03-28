from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from sweetify import sweetify
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test

from django.views import View
from django.contrib.auth.models import User, auth

from .forms import BookingForm, ServicesForm
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
        elif len(request.POST.get('username')) == 0 or len(request.POST.get('email')) == 0:
            messages.warning(request, 'Please fill in all the details!')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            cust = Customer.objects.create(name=name, phone=number, email_id=email)
            cust.save()
            messages.info(request, 'Successfully Registered. You can now login to your account.')
            return redirect('index')
    else:
        return render(request, "login.html")


@login_required
def logout(request):
    logout(request)
    return redirect(request.GET.get('next', '/'))
# def logout(request):
#     auth.logout(request)
#     return redirect('/')


def index(request):
    services = Service.objects.all()
    service_type_choices = Service.SERVICE_TYPE_CHOICES
    context = {
        'services': services,
        'service_type_choices': service_type_choices,
    }

    return render(request, 'index.html', context)


def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})


def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'service_detail.html', {'service': service})


def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, 'customer_detail.html', {'customer': customer})

@login_required()
def book_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    user = request.user
    if user.is_authenticated:
        email = request.user.email
    else:
        email = ''
    form = BookingForm(initial={'email':email})
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.service_id = service_id
            booking.featured_package_price = service.featured_package_price
            booking.save()
            sweetify.success(request, 'Hello World!', text='This is an example', persistent='Dismiss')
            messages.success(request, 'Booking has been created!')
            return redirect(reverse('booking_detail', args=(booking.id,)))
    return render(request, 'booking_form.html',{'form':form,'service':service})

@login_required()
def bookings(request):
    bookings = WeddingBooking.objects.all()
    email = request.user.email
    bookings = bookings.filter(email__exact=email)
    return render(request, 'bookings.html', {'bookings': bookings})

@login_required()
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


class About(View):
    def get(self, request):
        return render(request, 'about.html')



class Profile(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            try:
                customer = Customer.objects.filter(email_id=user.email).first()
                phone_number = customer.phone if customer else None
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
        print("hello test")
        user = request.user



        if user.is_authenticated:
            comment = request.POST['feedback']

            if comment == '':
                messages.warning(request, "please write something first and then submit feedback.")
                return redirect('feedback')

            else:
                email = user.email.split('@')[0]
                feedback = Feedback(name=email, feedback=comment)
                feedback.save()
                messages.success(request, 'Thanks for your feedback!')
                return redirect('feedback')

        else:
            messages.warning(request, "Please login first to post feedback.")
            return redirect('feedback')


class CancelBooking(View):
    def post(self, request):
        id = request.POST['booking_id']
        WeddingBooking.objects.filter(id=id).delete()
        messages.success(request, 'Your booking canceled successfully')
        return redirect(request.META['HTTP_REFERER'])



def service_add(request):
    form = ServicesForm()
    if not request.user.is_superuser:
        messages.warning(request, 'Only admins can add services.')
        return redirect(reverse('index'))
    if request.method == 'POST':
        form = ServicesForm(request.POST,request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            # booking.service_id = service_id
            # booking.featured_package_price = service.featured_package_price
            service.save()
            messages.success(request, 'Service has been created!')
            return redirect(reverse('index'))
    return render(request, 'addservices.html',{'form':form})


def booking_pdf(request, booking_id):
    # Get booking data for the specified booking_id
    booking = WeddingBooking.objects.get(id=booking_id)

    # Create a new PDF document with ReportLab
    pdf_canvas = canvas.Canvas('booking.pdf', pagesize=landscape(letter))

    # Create a table of booking details
    data = [
                ['Service', booking.service],
                ['Date', booking.date_booked],
                ['Name',booking.name],
                ['Phone',booking.phone],
                ['Email',booking.email],
                ['Price',booking.featured_package_price],
                ['Location',booking.location]
                # Add more booking details as needed
            ]

    # Customize the appearance of the table
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgrey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 14),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
                ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 12),
                ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
    ])

    # Create the table object
    table = Table(data, colWidths=[2*inch, 4*inch])

    # Apply the table style to the table object
    table.setStyle(table_style)

    # Add the table to the PDF canvas
    table.wrapOn(pdf_canvas, 0, 0)
    table.drawOn(pdf_canvas, 1*inch, 6*inch)
    # str = 'Thank you for choosing AdventureAwaits for your event needs!'
    # pdf_canvas.setFont('Helvetica-Bold', 18)
    # pdf_canvas.setFillColor(colors.black)  # set the fill color to black
    # pdf_canvas.drawString(2 * inch, 10 * inch, str)
    # Save and close the PDF
    pdf_canvas.save()

    # Return the PDF as a file download
    with open('booking.pdf', 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=booking.pdf'
        return response
