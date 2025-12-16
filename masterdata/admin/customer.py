from django.contrib import admin
from masterdata.models.customer import Customer

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('document', 'name', 'trade_name', 'state_registration', 'is_company', 'email', 'phone', 'city', 'price_table', 'payment_method', 'is_active', 'created_at', 'updated_at', 'created_by', 'updated_by',)
    list_display_links = ('document', 'name', 'trade_name')
    search_fields = ('document', 'name', 'trade_name',)
    list_filter = ('price_table', 'city', 'is_company', 'is_active',)
    list_editable = ('is_company', 'is_active',)
    list_per_page = 10
    readonly_fields = ('created_by', 'updated_by')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)
    