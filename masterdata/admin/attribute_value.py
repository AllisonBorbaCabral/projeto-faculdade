from django.contrib import admin
from masterdata.models.attribute_value import AttributeValue

class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    extra = 0
    fields = ('value', 'is_active', 'created_by', 'updated_by')
    readonly_fields = ('created_by', 'updated_by')