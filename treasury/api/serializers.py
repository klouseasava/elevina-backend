from rest_framework import serializers
from treasury.models import TreasuryAccount, TreasuryTransaction

class TreasuryAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreasuryAccount
        fields = ['id', 'total_balance']

class TreasuryTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreasuryTransaction
        fields = ['id', 'transaction_type', 'amount', 'date']
