from django.db import models
from locations.models.city import City
from .price_table import PriceTable
from .payment_method import PaymentMethod
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    trade_name = models.CharField(
        max_length=255,
        null=False, 
        blank=True,
    )
    document = models.CharField(
        max_length=18, 
        null=False,
        blank=False,
    )
    state_registration = models.CharField(
        max_length=30, 
        blank=True,
    )
    is_company = models.BooleanField(
        default=False,
    )
    email = models.EmailField(
        blank=True,
    )
    phone = models.CharField(
        max_length=30, 
        blank=True,
    )
    city = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    price_table = models.ForeignKey(
        PriceTable,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        default=True
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='customers_created',
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='customers_updated',
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
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        db_table='customer'
        constraints = [
            models.UniqueConstraint(
                fields=['document'],
                name='uq_customer_document'
            )
        ]