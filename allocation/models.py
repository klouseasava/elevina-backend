from django.db import models
from accounts.models import User

class Allocation(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    withdrawable = models.DecimalField(max_digits=12, decimal_places=2)
    locked_amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.receiver.username} - Withdrawable: {self.withdrawable} Locked: {self.locked_amount}"

# ----------------------
# Withdrawal model must be here, below Allocation
# ----------------------

class Withdrawal(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    allocation = models.ForeignKey(Allocation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.receiver.username} withdrew KES {self.amount} on {self.date.strftime('%Y-%m-%d')}"
