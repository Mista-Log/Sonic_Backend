from rest_framework import serializers
from .models import UserWallet

class UserWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWallet
        fields = "__all__"


