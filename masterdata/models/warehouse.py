from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Warehouse(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    allow_negative_stock = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='warehouses_created',
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='warehouses_updated',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(        
        auto_now=True,
        null=True,
        blank=True,
    )
    class Meta:
        verbose_name = 'Warehouse'
        verbose_name_plural = 'Warehouses'
        db_table='warehouse'
        constraints = [
            models.UniqueConstraint(
                fields=['name'],
                name='uq_warehouse_name'
            )
        ]