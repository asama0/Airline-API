from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.models import Flight, Customer, Booking
from ..serializers.serializers import FlightSerializer, CustomerSerializer,BookingSerializer


class BookFlightView(APIView):
    def post(self, request):
        flight_id = request.data.get('flight_id')
        customers = request.data.get('customers')

        if not flight_id or not customers:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            flight = Flight.objects.get(id=flight_id)
        except Flight.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if len(customers) > flight.available_seats:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        booking = Booking.objects.create(
            flight=flight,
            customers=customers,
            booking_status="on_hold"
        )

        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
