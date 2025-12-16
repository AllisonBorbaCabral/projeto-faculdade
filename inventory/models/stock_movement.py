from django.db import models
from django.contrib.auth.models import User
from masterdata.models.warehouse import Warehouse
from .stock_movement_type import StockMovementType

# Create your models here.
class StockMovement(models.Model):
    movement_type = models.ForeignKey(
        StockMovementType,
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )
    reference = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )  # NF, pedido, ajuste, etc
    movement_date = models.DateTimeField()
    notes = models.TextField(
        blank=True
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='stock_movements_created',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False
    )

    class Meta:
        verbose_name = 'Stock Movement'
        verbose_name_plural = 'Stock Movements'
        db_table = "stock_movement"
