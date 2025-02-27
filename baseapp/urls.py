from django.urls import path
from .views import UserWalletListCreateAPIView

urlpatterns = [
    path("wallet/", UserWalletListCreateAPIView.as_view(), name="connect-wallet"),
]