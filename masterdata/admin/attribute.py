from django.contrib import admin
from masterdata.models.attribute import Attribute
from .attribute_value import AttributeValueInline

# Register your models here.
@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at', 'updated_at', 'created_by', 'updated_by',)
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name', 'attribute_values__value',)
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    list_per_page = 10
    inlines = [AttributeValueInline]
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
