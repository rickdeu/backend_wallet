from django.urls import path
from .views import WalletBalanceView, AddBalanceView, TransferView, TransactionHistoryView

urlpatterns = [
    path('wallet/', WalletBalanceView.as_view(), name='wallet-balance'),
    path('wallet/add/', AddBalanceView.as_view(), name='add-balance'),
    path('transfer/', TransferView.as_view(), name='transfer'),
    path('transactions/', TransactionHistoryView.as_view(), name='transaction-history'),
]
