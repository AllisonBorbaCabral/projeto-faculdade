from django.contrib import admin
from inventory.models import StockMovementType

@admin.register(StockMovementType)
class StockMovementTypeAdmin(admin.ModelAdmin):
    list_display = ('code', 'direction', 'affects_stock', 'is_active')