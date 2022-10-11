from django.db import models


class transaction(models.TextChoices):
    DEBIT = "Débito"
    TICKET = "Boleto"
    FINANCING = "Financiamento"
    CREDIT = "Crédito"
    RECEIVING_LOAN = "Recebimento Empréstimo"
    SALES = "Vendas"
    RECEIPT_TED = "Recebimento TED"
    RECEIPT_DOC = "Recebimento DOC"
    RENT = "Aluguel"
    DEFAULT = "Nada"
    
    
class Documents(models.Model):
    type = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
    cpf = models.CharField(max_length=30)
    card = models.CharField(max_length=30)
    hour = models.CharField(max_length=30)
    owner_store = models.CharField(max_length=30)
    name_store= models.CharField(max_length=30)
