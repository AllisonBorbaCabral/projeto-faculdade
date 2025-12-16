from django.contrib import admin
from masterdata.models.product import Product
from .product_variant import ProductVariantInline

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'description', 'unit', 'track_stock', 'is_active', 'created_at', 'updated_at', 'created_by', 'updated_by',)
    list_display_links = ('sku', 'name',)
    search_fields = ('sku', 'name', 'product_variations__value',)
    list_filter = ('unit', 'track_stock', 'is_active',)
    list_editable = ('unit', 'track_stock', 'is_active',)
    list_per_page = 10
    inlines = [ProductVariantInline]
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
