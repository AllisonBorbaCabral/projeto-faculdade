from django.contrib import admin
from masterdata.models.unit import Unit

# Register your models here.
class ListUnits(admin.ModelAdmin):
    list_display = ('id', 'name', 'symbol', 'is_active', 'created_at', 'updated_at', 'created_by', 'updated_by',)
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name', 'symbol',)
    list_filter = ('is_active',)
    list_editable = ('symbol',)
    list_per_page = 10
    readonly_fields = ('created_by', 'updated_by')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Unit, ListUnits)