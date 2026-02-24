from rest_framework import generics, permissions
from treasury.models import TreasuryAccount, TreasuryTransaction
from .serializers import TreasuryAccountSerializer, TreasuryTransactionSerializer

class TreasuryAccountView(generics.ListAPIView):
    serializer_class = TreasuryAccountSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return TreasuryAccount.objects.all()

class TreasuryTransactionView(generics.ListAPIView):
    serializer_class = TreasuryTransactionSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return TreasuryTransaction.objects.all()
