from django.contrib import admin
from locations.models.state import State

# Register your models here.
class ListStates(admin.ModelAdmin):
    list_display = ('id', 'name', 'acronym', 'country', 'created_at', 'updated_at', 'created_by', 'updated_by',)
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name', 'acronym', 'country',)
    list_filter = ('is_active',)
    list_per_page = 10
    readonly_fields = ('created_by', 'updated_by')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(State, ListStates)