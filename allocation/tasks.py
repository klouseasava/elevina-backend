from celery import shared_task
from accounts.models import User
from .services import allocate_to_receiver

@shared_task
def run_monthly_allocation():
    receivers = User.objects.filter(role='RECEIVER')
    for receiver in receivers:
        allocate_to_receiver(receiver)
