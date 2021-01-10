from django.contrib import admin

from apps.tips.models.tips import Tips
from apps.tips.models.tips_products import TipsProduct


@admin.register(Tips)
class TipsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'total_price',
        'quantity',
        'payment_method'
    )
    list_filter = (
        'id',
    )


@admin.register(TipsProduct)
class TipsProductAdmin(admin.ModelAdmin):
    list_display = (
        'id_products',
        'id_tips',
    )
    list_filter = (
        'id_products',
        'id_tips',
    )

