from rest_framework import serializers
from allocation.models import Allocation, Withdrawal

class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        fields = ['id', 'receiver', 'total_amount', 'withdrawable', 'locked_amount', 'created_at']

class WithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdrawal
        fields = ['id', 'receiver', 'allocation', 'amount', 'date']
