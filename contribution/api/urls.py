from django.urls import path
from .views import ContributionListView

urlpatterns = [
    path('contributions/', ContributionListView.as_view(), name='contributions-list'),
]

