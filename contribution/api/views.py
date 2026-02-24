from rest_framework import generics, permissions
from contribution.models import Contribution
from .serializers import ContributionSerializer

class ContributionListView(generics.ListAPIView):
    serializer_class = ContributionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Contribution.objects.filter(donor=self.request.user)
