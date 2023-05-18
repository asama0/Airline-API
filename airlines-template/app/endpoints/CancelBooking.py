from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.models import Booking
from ..serializers.serializers import BookingSerializer


class CancelBookingView(APIView):
    def put(self, request):
        booking_id = request.data.get('booking_id')

        if not booking_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            booking = Booking.objects.get(id=booking_id)
        except Booking.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        booking.booking_status = "cancelled"
        booking.save()

        # Refund the customer

        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)
