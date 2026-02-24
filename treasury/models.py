from django.db import models

class TreasuryAccount(models.Model):
    total_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

class TreasuryTransaction(models.Model):
    TRANSACTION_TYPE = (
        ('IN', 'Incoming'),
        ('OUT', 'Outgoing'),
    )
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
