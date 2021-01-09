from default.models.base_model import BaseModel
from apps.products.models.category import Category
from django.db import models

class Products(BaseModel):

    code = models.CharField('SKU', max_length=250, blank=False, null=False, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=100, null=False, blank=False)
    quantity = models.IntegerField('Stock Quantity', null=False, blank=False)
    price = models.DecimalField('Price', null=False, blank=False, decimal_places=2, max_digits=50)
    bill_id = models.ManyToManyField('tips.Tips', through='tips.TipsProduct')

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name + '-' + str(self.category)
