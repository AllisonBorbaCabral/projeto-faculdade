from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PriceTable(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    code = models.CharField(
        max_length=30,
    )
    discount_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
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
        related_name='price_tables_created',
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='price_tables_updated',
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
        verbose_name = 'Price Table'
        verbose_name_plural = 'Price Tables'
        db_table='price_table'
        constraints = [
            models.UniqueConstraint(
                fields=['code'],
                name='uq_price_table_code'
            ),
        ]