from rest_framework import generics, permissions
from vouchers.models import Voucher
from .serializers import VoucherSerializer

class VoucherListView(generics.ListAPIView):
    serializer_class = VoucherSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Voucher.objects.filter(donor=self.request.user)
