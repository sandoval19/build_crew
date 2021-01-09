from django.contrib import admin
from apps.clients.models.clients import Clients


class ClientAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'name', 'last_name', 'address', 'phone')


admin.site.register(Clients, ClientAdmin)