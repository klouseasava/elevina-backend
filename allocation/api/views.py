from rest_framework import generics, permissions
from allocation.models import Allocation, Withdrawal
from .serializers import AllocationSerializer, WithdrawalSerializer
from allocation.services import withdraw_funds
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class AllocationListView(generics.ListAPIView):
    serializer_class = AllocationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Allocation.objects.filter(receiver=self.request.user)

class WithdrawFundsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        allocation_id = request.data.get('allocation_id')
        amount = float(request.data.get('amount'))
        try:
            withdrawal = withdraw_funds(self.request.user, allocation_id, amount)
            return Response({
                'id': withdrawal.id,
                'amount': withdrawal.amount,
                'allocation': withdrawal.allocation.id,
                'date': withdrawal.date
            })
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
