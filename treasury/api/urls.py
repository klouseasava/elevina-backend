from django.urls import path
from .views import TreasuryAccountView, TreasuryTransactionView

urlpatterns = [
    path('accounts/', TreasuryAccountView.as_view(), name='treasury-accounts'),
    path('transactions/', TreasuryTransactionView.as_view(), name='treasury-transactions'),
]
