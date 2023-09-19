from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'user_name', 'description')

admin.site.register(Item, ItemAdmin)
