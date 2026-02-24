from celery import shared_task
from accounts.models import User
from .services import process_donation

@shared_task
def run_monthly_deductions():
    donors = User.objects.filter(role='DONOR')
    for donor in donors:
        process_donation(donor)
