from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import uuid

from ..models.models import Booking, PaymentProvider
from ..serializers.serializers import BookingSerializer


class PayBookingView(APIView):
    def post(self, request, booking_id):
        try:
            booking = Booking.objects.get(id=booking_id)
        except Booking.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        psp_id = request.data.get('psp_id')

        if not psp_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        try:
            payment_provider = PaymentProvider.objects.get(id=psp_id)
        except PaymentProvider.DoesNotExist:
            return Response({"error": "Payment Provider does not exist"}, status=status.HTTP_404_NOT_FOUND)

        try:
            transaction = str(uuid.uuid4())
            
        except Exception as e:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

        return Response({'transaction_id': transaction}, status=status.HTTP_201_CREATED)
