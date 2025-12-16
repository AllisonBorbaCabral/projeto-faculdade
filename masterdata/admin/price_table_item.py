from django.contrib import admin
from masterdata.models.price_table_item import PriceTableItem

class PriceTableItemInline(admin.TabularInline):
    model = PriceTableItem
    extra = 0
    fields = ('product_variant', 'price', 'is_active', 'created_by', 'updated_by')
    readonly_fields = ('created_by', 'updated_by')