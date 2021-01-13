from default.models.base_model import BaseModel
from django.db import models
import secrets
import uuid
import os


def customer_image_file_path(instance, file_name):
    """Generate file path for new customer image"""
    ext = file_name.split('.')[-1]
    file_name = f'{uuid.uuid4()}.{ext}'

    return os.path.join('images/', file_name)


class Clients(BaseModel):

    # CLIENT_TYPES = (
    #     ('G', 'Gold'),
    #     ('S', 'Silver'),
    #     ('B', 'Bronze')
    # )
    
    identifier = models.CharField('Identifier', max_length=20, null=False, blank=False, unique=True)
    name = models.CharField('Name', max_length=60, null=False, blank=False)
    last_name = models.CharField('Last Name', max_length=60, null=False, blank=False)
    address = models.CharField('Address', max_length=100, null=True, blank=True)
    phone = models.CharField('Phone Number', max_length=20, null=False, blank=False)
    phote = models.ImageField('Profile photo', upload_to=customer_image_file_path, blank=True, null=True)
    # classification = models.CharField(max_length=1, null=True, blank=True, choices=CLIENT_TYPES)

    class Meta:
        ordering = ['identifier']

    def __str__(self):
        return self.name

