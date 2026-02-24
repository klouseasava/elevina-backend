from .models import Contribution
from accounts.models import User
from treasury.models import TreasuryAccount, TreasuryTransaction
from vouchers.services import create_voucher  # <-- import voucher service
from decimal import Decimal

def calculate_deduction(user: User) -> Decimal:
    """
    Progressive deduction based on net pay.
    """
    income = user.net_pay

    if income >= 100000:
        deduction = income * Decimal('0.15')  # 15%
    elif income >= 50000:
        deduction = income * Decimal('0.10')  # 10%
    elif income >= 20000:
        deduction = income * Decimal('0.05')  # 5%
    else:
        deduction = Decimal('0')

    return deduction

def process_donation(user: User):
    """
    Deduct from donor, save contribution, send to treasury,
    and reward a voucher.
    """
    amount = calculate_deduction(user)
    if amount <= 0:
        return None

    # Save contribution record
    contribution = Contribution.objects.create(donor=user, amount=amount)

    # Add to Treasury
    treasury, _ = TreasuryAccount.objects.get_or_create(id=1)
    treasury.total_balance += amount
    treasury.save()

    # Log transaction
    TreasuryTransaction.objects.create(
        transaction_type='IN',
        amount=amount
    )

    # Give donor a voucher worth 5% of contribution
    voucher_value = amount * Decimal('0.05')
    create_voucher(user, voucher_value)

    return contribution
