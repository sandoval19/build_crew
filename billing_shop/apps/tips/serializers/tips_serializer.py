from rest_framework import serializers
from apps.tips.models.tips import Tips


class TipsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tips
        fields = [
            'id_clients',
            'id_products',
            'total_price',
            'payment_method',
            'quantity',
        ]
