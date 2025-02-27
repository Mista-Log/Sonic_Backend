from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import UserWallet
from rest_framework import generics
from .serializers import UserWalletSerializer


# class UserWalletDetailView(generics.RetrieveUpdateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserWalletSerializer

#     def get_object(self):
#         return UserWallet.objects.get(user=self.request.user)


class UserWalletListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserWalletSerializer


    def get_queryset(self):
        
        return UserWallet.objects.filter(user=self.request.user)

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)



# class UserWalletView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         try:
#             wallet = UserWallet.objects.get(user=request.user)
#             wallet_data = {
#                 "wallet_address": wallet.wallet_address,
#                 "balance": wallet.balance,
#                 "currency": wallet.currency,
#                 "created_at": wallet.created_at,
#             }
#             return Response(wallet_data, status=status.HTTP_200_OK)
#         except UserWallet.DoesNotExist:
#             return Response({"error": "Wallet not found"}, status=status.HTTP_404_NOT_FOUND)

#     def post(self, request):
#         wallet_address = request.data.get("wallet_address")
#         balance = request.data.get("balance")
#         currency = request.data.get("currency")

#         if not wallet_address:
#             return Response({"error": "Wallet address is required"}, status=status.HTTP_400_BAD_REQUEST)

#         wallet, created = UserWallet.objects.get_or_create(user=request.user)
#         wallet.wallet_address = wallet_address
#         wallet.balance = balance
#         wallet.currency = currency
#         wallet.save()

#         return Response({"message": "Wallet connected successfully", "wallet_address": wallet_address})


# class ConnectWalletView(APIView):
#     # permission_classes = [IsAuthenticated]

#     def post(self, request):
#         wallet_address = request.data.get("wallet_address")
#         if not wallet_address:
#             return Response({"error": "Wallet address is required"}, status=status.HTTP_400_BAD_REQUEST)

#         wallet, created = UserWallet.objects.get_or_create(user=request.user)
#         wallet.wallet_address = wallet_address
#         wallet.save()

#         return Response({"message": "Wallet connected successfully", "wallet_address": wallet_address})