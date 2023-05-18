from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from ..models.models import Booking
from ..serializers.serializers import BookingSerializer

class BookingDetailsView(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get(self, request, *args, **kwargs):
        try:
            booking = self.queryset.get(pk=kwargs["booking_id"])
            response_data = BookingSerializer(booking).data
            return Response(response_data, status=status.HTTP_200_OK)
        except Booking.DoesNotExist:
            return Response("Booking not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_503_SERVICE_UNAVAILABLE)
