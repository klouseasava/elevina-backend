from django.urls import path
from .views import AllocationListView, WithdrawFundsView

urlpatterns = [
    path('allocations/', AllocationListView.as_view(), name='allocations-list'),
    path('withdraw/', WithdrawFundsView.as_view(), name='withdraw-funds'),
]
