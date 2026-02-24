from django.db import models
from accounts.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .services import classify_user


class TaxRecord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    annual_income = models.DecimalField(max_digits=12, decimal_places=2)
    tax_paid = models.DecimalField(max_digits=12, decimal_places=2)
    employer_name = models.CharField(max_length=255, null=True, blank=True)
    last_synced = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Tax Record"

@receiver(post_save, sender=TaxRecord)
def update_user_role(sender, instance, **kwargs):
    user = instance.user
    user.tax_paid = instance.tax_paid
    user.net_pay = instance.annual_income / 12
    user.save()

    classify_user(user)

