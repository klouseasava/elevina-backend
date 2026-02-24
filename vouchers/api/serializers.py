from rest_framework import serializers
from vouchers.models import Voucher

class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = ['id', 'donor', 'code', 'value', 'redeemed', 'expiry_date', 'created_at']
