from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StockMovementType(models.Model):
    code = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    description = models.CharField(
        max_length=255
    )
    affects_stock = models.BooleanField(
        default=True
    )
    affects_financial = models.BooleanField(
        default=False
    )
    direction = models.CharField(
        max_length=3,
        choices=[
            ('IN', 'Entrada'),
            ('OUT', 'Saída'),
            ('TRF', 'Transferência'),
        ]
    )
    is_active = models.BooleanField(
        default=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='stock_movement_types_created',
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='stock_movement_types_updated',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False
    )
    updated_at = models.DateTimeField(   
        auto_now=True,     
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Stock Movement Type'
        verbose_name_plural = 'Stock Movement Types'
        db_table='stock_movement_type'