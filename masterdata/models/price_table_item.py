from django.db import models
from .price_table import PriceTable
from .product_variant import ProductVariant
from django.contrib.auth.models import User

# Create your models here.
class PriceTableItem(models.Model):
    price_table = models.ForeignKey(
        PriceTable,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name="items"
    )
    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )
    price = models.DecimalField(
        max_digits=15,
        decimal_places=4,
        null=False,
        blank=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='price_table_items_created',
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='price_table_items_updated',
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
    class Meta:
        verbose_name = 'Price Table Item'
        verbose_name_plural = 'Price Table Items'
        db_table='price_table_item'
        constraints = [
            models.UniqueConstraint(
                fields=['price_table', 'product_variant'],
                name='uq_price_table_variant'
            )
        ]