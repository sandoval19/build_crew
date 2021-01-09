from default.models.base_model import BaseModel
from django.db import models


class Category(BaseModel):
    name = models.CharField('Category', unique=True, null=False, max_length=100)

    def __str__(self):
        return self.name
