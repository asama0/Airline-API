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
        number_of_tickets = request.query_params.get('number_of_tickets')

        if not departure_airport or not destination_airport or not departure_datetime:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            flights = Flight.objects.filter(
                departure_airport=departure_airport,
                destination_airport=destination_airport,
                departure_datetime__lte=departure_datetime,
            ).order_by('departure_datetime')
        except Flight.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if number_of_tickets:
            flights = flights.filter(
                available_seats__gte=number_of_tickets
            )

        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
