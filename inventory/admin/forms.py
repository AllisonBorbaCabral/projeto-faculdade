from django import forms
from inventory.models import StockMovementType
from masterdata.models import ProductVariant

class StockMovementAdminForm(forms.Form):
    movement_type = forms.ModelChoiceField(
        queryset=StockMovementType.objects.filter(is_active=True)
    )
    warehouse = forms.ModelChoiceField(
        queryset=None
    )
    movement_date = forms.DateTimeField()
    reference = forms.CharField(required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False)

    # itens (simples para admin)
    product_variant = forms.ModelChoiceField(
        queryset=ProductVariant.objects.all()
    )
    quantity = forms.DecimalField()
    unit_cost = forms.DecimalField(required=False)

    def __init__(self, *args, **kwargs):
        warehouse_qs = kwargs.pop('warehouse_qs', None)
        super().__init__(*args, **kwargs)

        if warehouse_qs:
            self.fields['warehouse'].queryset = warehouse_qs
