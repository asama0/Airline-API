from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.models import Booking, Ticket
from ..serializers.serializers import BookingSerializer, TicketSerializer


class ConfirmBookingView(APIView):
    def put(self, request):
        booking_id = request.data.get('booking_id')
        success_key = request.data.get('success_key')

        if not booking_id or not success_key:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            booking = Booking.objects.get(id=booking_id)
        except Booking.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if booking.success_key != success_key:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        booking.booking_status = "confirmed"
        booking.save()

        tickets = []
        for customer in booking.customers.all():
            ticket = Ticket.objects.create(
                booking=booking,
                customer=customer,
                seat_number=1
            )
            tickets.append(ticket)

        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)
