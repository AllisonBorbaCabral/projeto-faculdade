from django.contrib import admin
from masterdata.models.product_variant import ProductVariant
from .product_variant_attribute import ProductVariantAttributeItemInline

# Register your models here.
@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('sku', 'product', 'barcode','standard_cost', 'is_active', 'created_at', 'updated_at', 'created_by', 'updated_by',)
    list_display_links = ('sku', 'product',)
    search_fields = ('sku', 'product', 'ProductVariantAttribute__value',)
    list_filter = ('is_active',)
    list_per_page = 10
    inlines = [ProductVariantAttributeItemInline]
    readonly_fields = ('created_by', 'updated_by')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if not instance.pk:
                instance.created_by = request.user
            instance.updated_by = request.user
            instance.save()
        
        for obj in formset.deleted_objects:
            obj.delete()

        formset.save_m2m()


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 0
    readonly_fields = ('created_by', 'updated_by')