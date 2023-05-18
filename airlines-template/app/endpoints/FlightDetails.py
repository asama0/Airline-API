from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.models import Flight
from ..serializers.serializers import FlightSerializer


class FlightDetailsView(APIView):
    def get(self, request, flight_id):
        try:
            flight = Flight.objects.get(id=flight_id)
        except Flight.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FlightSerializer(flight)
        return Response(serializer.data, status=status.HTTP_200_OK)

