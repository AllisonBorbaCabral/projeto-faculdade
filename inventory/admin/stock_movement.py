from django.urls import path
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib import admin, messages
from django.template.response import TemplateResponse
from inventory.services.stock_service import (
    create_stock_in,
    create_stock_out
)
from inventory.models import StockMovement
from .forms import StockMovementAdminForm


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    change_list_template = 'admin/inventory/stock_movement_create.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'create/',
                self.admin_site.admin_view(self.create_stock_movement),
                name='inventory_stockmovement_create',
            ),
        ]
        return custom_urls + urls

    def create_stock_movement(self, request):
        if request.method == 'POST':
            form = StockMovementAdminForm(request.POST)
            if form.is_valid():
                movement_type = form.cleaned_data['movement_type']

                item = {
                    'product_variant': form.cleaned_data['product_variant'],
                    'quantity': form.cleaned_data['quantity'],
                    'unit_cost': form.cleaned_data['unit_cost'],
                }

                try:
                    if movement_type.direction == 'IN':
                        create_stock_in(
                            movement_type=movement_type,
                            warehouse=form.cleaned_data['warehouse'],
                            items=[item],
                            reference=form.cleaned_data['reference'],
                            movement_date=form.cleaned_data['movement_date'],
                            notes=form.cleaned_data['notes'],
                        )
                    else:
                        create_stock_out(
                            movement_type=movement_type,
                            warehouse=form.cleaned_data['warehouse'],
                            items=[item],
                            reference=form.cleaned_data['reference'],
                            movement_date=form.cleaned_data['movement_date'],
                            notes=form.cleaned_data['notes'],
                        )

                    self.message_user(
                        request,
                        'Stock movement created successfully.',
                        messages.SUCCESS,
                    )
                    return redirect('..')

                except Exception as e:
                    self.message_user(
                        request,
                        str(e),
                        messages.ERROR,
                    )
        else:
            form = StockMovementAdminForm(
                initial={'movement_date': timezone.now()}
            )

        context = {
            'form': form,
            'title': 'Create Stock Movement',
        }
        return TemplateResponse(
            request,
            'admin/inventory/stock_movement_form.html',
            context,
        )