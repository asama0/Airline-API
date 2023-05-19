"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .endpoints.FlightDetails import FlightDetailsView
from .endpoints.FlightSearch import FlightSearchView
from .endpoints.PayBooking import PayBookingView
from .endpoints.BookFlight import BookFlightView
from .endpoints.ConfirmBooking import ConfirmBookingView
from .endpoints.UpdateBooking import UpdateBookingView
from .endpoints.CancelBooking import CancelBookingView
from .endpoints.PaymentProvidersList import PaymentProvidersListView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/flight/<int:flight_id>', FlightDetailsView.as_view()),
    path('api/flights', FlightSearchView.as_view()),
    path('api/paybooking/<int:booking_id>', PayBookingView.as_view(), name='pay-booking'),

    path('api/book', BookFlightView.as_view()),
    path('api/booking/<int:booking_id>', UpdateBookingView.as_view()),

    path('api/confirmbooking', ConfirmBookingView.as_view()),
    path('api/cancelbooking', CancelBookingView.as_view(), name='cancel_booking'),
    path('api/paymentproviders', PaymentProvidersListView.as_view())

]
