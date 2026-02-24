from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    national_id = models.CharField(max_length=20, unique=True)
    kra_pin = models.CharField(max_length=20, unique=True)

    ROLE_CHOICES = (
        ('DONOR', 'Donor'),
        ('RECEIVER', 'Receiver'),
        ('UNCLASSIFIED', 'Unclassified'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='UNCLASSIFIED')

    net_pay = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    tax_paid = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    is_employed = models.BooleanField(default=False)

    def __str__(self):
        return self.username
