from default.models.base_model import BaseModel
from apps.clients.models.clients import Clients
from django.db import models


class Tips(BaseModel):

    PAYMENT_CHOICES = (
        ('0', 'Cash'),
        ('1', 'Credit Card'),
        ('2', 'Debit Card'),
    )
    id_clients = models.ForeignKey(Clients, on_delete=models.CASCADE)
    id_products = models.ManyToManyField('products.Products', through='tips.TipsProduct')
    total_price = models.DecimalField('Total price', decimal_places=2, max_digits=50)
    payment_method = models.CharField('Payment Method', max_length=2, null=False, unique=False, choices=PAYMENT_CHOICES)
    quantity = models.IntegerField('Products Quantity', null=False, unique=False)

    class Meta:
        ordering = ['-create_at']
