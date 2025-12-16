from django.contrib import admin
from masterdata.models.product_variant_attribute import ProductVariantAttribute

@admin.register(ProductVariantAttribute)
class ProductVariantAttributeAdmin(admin.ModelAdmin):
    list_display = ('product_variant', 'attribute', 'attribute_value', 'is_active', 'created_at', 'updated_at', 'created_by', 'updated_by',)
    list_display_links = ('product_variant', 'attribute',)
    search_fields = ('product_variant', 'attribute', 'attribute_value',)
    list_filter = ('product_variant', 'is_active',)
    list_per_page = 10
    readonly_fields = ('created_by', 'updated_by')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


class ProductVariantAttributeItemInline(admin.TabularInline):
    model = ProductVariantAttribute
    extra = 0
    readonly_fields = ('created_by', 'updated_by')