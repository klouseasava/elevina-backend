import random
import string
from datetime import datetime, timedelta
from .models import Voucher
from accounts.models import User

def generate_voucher_code(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def create_voucher(donor: User, value: float, days_valid=30):
    code = generate_voucher_code()
    expiry_date = datetime.now().date() + timedelta(days=days_valid)

    voucher = Voucher.objects.create(
        donor=donor,
        code=code,
        value=value,
        expiry_date=expiry_date
    )
    return voucher
