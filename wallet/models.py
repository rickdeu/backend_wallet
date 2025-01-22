from django.db import models
from django.utils.timezone import now
from base.models import BaseModel
from custom_user.models import User
from wallet.helpers.enums import TransactionType

class Wallet(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def add_balance(self, amount):
        self.balance += amount
        self.save()

    def deduct_balance(self, amount):
        if self.balance < amount:
            raise ValueError("Saldo insuficiente.")
        self.balance -= amount
        self.save()

class Transaction(BaseModel):
    sender = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='sent_transactions')
    receiver = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='received_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=now)
    transaction_type = models.CharField(
        max_length=20, choices=TransactionType.choices, default=TransactionType.TRANSFER
    )

    def save(self, *args, **kwargs):
        if self.sender == self.receiver:
            raise ValueError("O remetente e o destinatário não podem ser iguais.")
        if self.amount <= 0 and self.sender.balance < self.amount:
            raise ValueError("saldo insuficiente/valor da transação invalido")
        super().save(*args, **kwargs)
