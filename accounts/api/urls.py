from django.urls import path
from .views import UserDetailView
from .register import RegisterView

urlpatterns = [
    path('me/', UserDetailView.as_view(), name='user-detail'),
    path('register/', RegisterView.as_view(), name='register'),
]
