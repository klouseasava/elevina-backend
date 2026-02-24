from decimal import Decimal
from accounts.models import User
from allocation.models import Allocation, Withdrawal
from treasury.models import TreasuryAccount, TreasuryTransaction

MAX_ALLOCATION = Decimal('10000')
WITHDRAW_PERCENT = Decimal('0.5')  # 50%

def allocate_to_receiver(receiver: User):
    """
    Allocate funds to a receiver from Treasury.
    """
    treasury, _ = TreasuryAccount.objects.get_or_create(id=1)

    if treasury.total_balance <= 0:
        return None  # No funds to distribute

    # Determine withdrawable and locked
    withdrawable = MAX_ALLOCATION * WITHDRAW_PERCENT
    locked_amount = MAX_ALLOCATION * (1 - WITHDRAW_PERCENT)

    # Adjust if Treasury has less than MAX_ALLOCATION
    if treasury.total_balance < MAX_ALLOCATION:
        ratio = treasury.total_balance / MAX_ALLOCATION
        withdrawable *= ratio
        locked_amount *= ratio

    # Deduct from Treasury
    treasury.total_balance -= (withdrawable + locked_amount)
    treasury.save()

    # Log Treasury OUT transaction
    TreasuryTransaction.objects.create(
        transaction_type='OUT',
        amount=(withdrawable + locked_amount)
    )

    # Save allocation record
    allocation = Allocation.objects.create(
        receiver=receiver,
        total_amount=withdrawable + locked_amount,
        withdrawable=withdrawable,
        locked_amount=locked_amount
    )

    return allocation


def withdraw_funds(receiver: User, allocation_id: int, amount: float):
    """
    Allows receiver to withdraw from their withdrawable amount.
    """
    allocation = Allocation.objects.get(id=allocation_id, receiver=receiver)

    if amount > allocation.withdrawable:
        raise ValueError("Cannot withdraw more than the withdrawable amount")

    # Deduct from allocation
    allocation.withdrawable -= amount
    allocation.save()

    # Deduct from Treasury
    treasury, _ = TreasuryAccount.objects.get_or_create(id=1)
    if treasury.total_balance < amount:
        raise ValueError("Treasury has insufficient funds")

    treasury.total_balance -= amount
    treasury.save()

    # Log Treasury transaction
    TreasuryTransaction.objects.create(
        transaction_type='OUT',
        amount=amount
    )

    # Record withdrawal
    withdrawal = Withdrawal.objects.create(
        receiver=receiver,
        allocation=allocation,
        amount=amount
    )

    return withdrawal
