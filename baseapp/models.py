from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class UserWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="wallet")
    wallet_address = models.CharField(max_length=255, unique=True, blank=True, null=True)
    balance = models.DecimalField(max_digits=20, decimal_places=8, default=0.0)
    currency = models.CharField(max_length=10, default="SOL")  # Default to Bitcoin
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Wallet - {self.wallet_address}"




