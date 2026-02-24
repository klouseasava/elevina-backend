from rest_framework import serializers
from contribution.models import Contribution

class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = ['id', 'donor', 'amount', 'date']
