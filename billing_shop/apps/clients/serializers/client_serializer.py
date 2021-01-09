from rest_framework import serializers
from apps.clients.models.clients import Clients

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clients
        fields = ['identifier', 'name', 'last_name', 'address', 'phone']
