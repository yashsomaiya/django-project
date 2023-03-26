from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path ( '' , views.index , name = 'index' ) ,
    path("login", views.login, name="login"),
    path("accounts/login",views.accountlogin, name="accountlogin"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout, name="logout"),
    path ( 'service/' , views.Service , name = 'services' ) ,
    path ( 'service/<uuid:service_id>/' , views.service_detail , name = 'service_detail' ) ,
    path ( 'customer/<uuid:customer_id>/' , views.customer_detail , name = 'customer_detail' ) ,
    path ( 'book/<uuid:service_id>/' , views.book_service , name = 'book_service' ) ,
    path ( 'bookings/' , views.bookings , name = 'bookings' ) ,
    path ( 'booking/<uuid:booking_id>/' , views.booking_detail , name = 'booking_detail' ) ,
    path ( 'booking/<uuid:booking_id>/pay/' , views.pay_booking , name = 'pay_booking' ) ,
    path('about', About.as_view(), name="about"),
    path('contact', Contact.as_view(), name="contact"),
    path('feedback', Feedbacks.as_view(), name="feedback"),
    path('profile', Profile.as_view(), name="profile"),
    path('bookings/cancel_booking', CancelBooking.as_view(), name="cancel_booking"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
