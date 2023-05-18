from rest_framework import serializers
from ..models.models import Flight, Booking, Customer, Ticket, PaymentProvider, Aircraft,Airport

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class PaymentProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentProvider
        fields = '__all__'

class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    destination_airport = AirportSerializer()
    departure_airport = AirportSerializer()
    aircraft = AircraftSerializer()

    class Meta:
        model = Flight
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    flight = FlightSerializer()
    customer = CustomerSerializer()
    payment_provider = PaymentProviderSerializer()

    class Meta:
        model = Booking
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    booking = BookingSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Ticket
        fields = '__all__'


