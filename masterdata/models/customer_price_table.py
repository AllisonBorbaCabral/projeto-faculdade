from django.db import models
from .customer import Customer
from .price_table import PriceTable
from django.contrib.auth.models import User

# Create your models here.
class CustomerPriceTable(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )
    price_table = models.ForeignKey(
        PriceTable,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    valid_from = models.DateField(
        null=True, 
        blank=True,
    )
    valid_to = models.DateField(
        null=True, 
        blank=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='customer_price_tables_created',
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='customer_price_tables_updated',
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
        verbose_name = 'Customer Price Table'
        verbose_name_plural = 'Customer Price Tables'
        db_table='customer_price_table'
        constraints = [
            models.UniqueConstraint(
                fields=['customer'],
                name='uq_customer_price_table'
            )
        ]
