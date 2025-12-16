from django.db import models
from .stock_movement import StockMovement
from masterdata.models.product_variant import ProductVariant

# Create your models here.
class StockMovementItem(models.Model):
    movement = models.ForeignKey(
        StockMovement,
        null=False,
        blank=False,
        related_name='items',
        on_delete=models.PROTECT,
    )
    product_variant = models.ForeignKey(
        ProductVariant,
        null=False,
        blank=False,
        related_name='movements',
        on_delete=models.PROTECT
    )
    quantity = models.DecimalField(
        max_digits=14,
        decimal_places=4,
        null=False,
        blank=False
    )
    unit_cost = models.DecimalField(
        max_digits=14,
        decimal_places=4,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Stock Movement Item'
        verbose_name_plural = 'Stock Movement Items'
        db_table = 'stock_movement_item'
        indexes = [
            models.Index(fields=['product_variant']),
            models.Index(fields=['movement']),
        ]
