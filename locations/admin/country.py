from django.contrib import admin
from locations.models.country import Country

# Register your models here.
class ListCountries(admin.ModelAdmin):
    list_display = ('id', 'name', 'idd', 'acronym', 'created_at', 'updated_at', 'created_by', 'updated_by',)
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name', 'acronym',)
    list_filter = ('is_active',)
    list_editable = ('idd', 'acronym',)
    list_per_page = 10
    readonly_fields = ('created_by', 'updated_by')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Country, ListCountries)