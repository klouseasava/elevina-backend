from django.db import models
from accounts.models import User

class Contribution(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor.username} - KES {self.amount} - {self.date.strftime('%Y-%m-%d')}"
