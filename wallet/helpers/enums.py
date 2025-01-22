from django.db import models


class TransactionType(models.TextChoices):
    TRANSFER = "TRANSFER", "Transferência"
    ADD_FUNDS = "ADD_FUNDS", "Adicionar Fundos"
    DEDUCT_FUNDS = "DEDUCT_FUNDS", "Retirar Fundos"