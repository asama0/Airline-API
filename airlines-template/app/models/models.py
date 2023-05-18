from django.db import models
from datetime import timedelta

class Airport(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    time_zone = models.IntegerField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    passport_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email_address = models.EmailField()
    date_of_birth = models.DateField()
    home_address = models.CharField(max_length=255)
    allergies = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class PaymentProvider(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    account_id = models.IntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Aircraft(models.Model):
    tail_number = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    number_of_seats = models.IntegerField()

    def __str__(self):
        return f"{self.type} - {self.tail_number}"

class Flight(models.Model):
    destination_airport = models.ForeignKey(Airport, related_name='destination_flights', on_delete=models.CASCADE)
    departure_airport = models.ForeignKey(Airport, related_name='departure_flights', on_delete=models.CASCADE)
    flight_number = models.CharField(max_length=255)
    duration = models.DurationField()
    departure_datetime = models.DateTimeField()
    price_per_seat = models.IntegerField()
    cost_per_seat = models.IntegerField()
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.flight_number} - {self.departure_airport} to {self.destination_airport}"

class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_provider = models.ForeignKey(PaymentProvider, on_delete=models.CASCADE)
    price = models.FloatField()
    booking_datetime = models.DateTimeField(auto_now_add=True)
    booking_status = models.IntegerField()
    transaction_id = models.IntegerField()
    success_key = models.CharField(max_length=255)

    def __str__(self):
        return f"Booking {self.id} - {self.customer} - {self.flight}"

class Ticket(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seat_number = models.IntegerField()

    def __str__(self):
        return f"Ticket {self.id} - Booking {self.booking.id} - Seat {self.seat_number}"

