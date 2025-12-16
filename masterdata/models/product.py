from .unit import Unit
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    sku = models.CharField(
        max_length=60,
        null=False,
        blank=False,
    )
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    description = models.TextField(
        blank=True,
    )
    unit = models.ForeignKey(
        Unit, 
        on_delete=models.PROTECT,
        related_name='products',
    )
    track_stock = models.BooleanField(
        default=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='products_created',
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='products_updated',
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
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table='product'
        constraints = [
            models.UniqueConstraint(
                fields=['sku'],
                name='uq_product_sku'
            ),
        ]