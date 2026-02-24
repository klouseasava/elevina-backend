from django.urls import path
from .views import VoucherListView

urlpatterns = [
    path('vouchers/', VoucherListView.as_view(), name='vouchers-list'),
]
