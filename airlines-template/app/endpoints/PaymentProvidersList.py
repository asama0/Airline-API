from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.models import PaymentProvider
from ..serializers.serializers import PaymentProviderSerializer


class PaymentProvidersListView(APIView):
    def get(self, request):
        payment_providers = PaymentProvider.objects.all()

        serializer = PaymentProviderSerializer(payment_providers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
