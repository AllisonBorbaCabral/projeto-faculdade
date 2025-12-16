from django.db import models
from .product import Product
from .attribute_value import AttributeValue
from django.contrib.auth.models import User

# Create your models here.
class ProductVariant(models.Model):
    sku = models.CharField(
        max_length=60,
        null=False,
        blank=False,
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.PROTECT,
        related_name='product_variations',
    )
    barcode = models.CharField(
        max_length=60, 
        blank=True
    )
    attributes = models.ManyToManyField(
        AttributeValue,
        through='ProductVariantAttribute'
    )
    standard_cost = models.DecimalField(
        max_digits=15,
        decimal_places=4,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        default=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='product_variations_created',
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='product_variations_updated',
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
        return self.product.name

    class Meta:
        verbose_name = 'Product Variant'
        verbose_name_plural = 'Product Variants'
        db_table='product_variant'
        constraints = [
            models.UniqueConstraint(
                fields=['sku'],
                name='uq_product_variant_sku'
            ),
        ]