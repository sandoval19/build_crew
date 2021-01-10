from default.models.base_model import BaseModel
from apps.products.models.products import Products
from apps.tips.models.tips import Tips
from django.db import models


class TipsProduct(BaseModel):
    id_products = models.ForeignKey(Products, on_delete=models.CASCADE)
    id_tips = models.ForeignKey(Tips, on_delete=models.CASCADE)
