from django.utils.dateparse import parse_datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.models import Flight
from ..serializers.serializers import FlightSerializer

class FlightSearchView(APIView):
    def get(self, request):
        departure_airport = request.query_params.get('departure_airport')
        destination_airport = request.query_params.get('destination_airport')
        departure_datetime = request.query_params.get('departure_datetime')
        

        if not departure_airport or not destination_airport or not departure_datetime:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        departure_datetime = parse_datetime(departure_datetime)

        flights = Flight.objects.filter(
            departure_airport__name=departure_airport,
            destination_airport__name=destination_airport,
            departure_datetime__lte=departure_datetime,
        ).order_by('departure_datetime')

        

        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
