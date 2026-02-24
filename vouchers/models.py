from django.db import models
from accounts.models import User

class Voucher(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, unique=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    redeemed = models.BooleanField(default=False)
    expiry_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.donor.username} - KES {self.value}"
