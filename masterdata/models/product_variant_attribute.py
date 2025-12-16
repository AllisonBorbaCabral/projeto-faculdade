from django.db import models
from .attribute import Attribute
from .product_variant import ProductVariant
from .attribute_value import AttributeValue
from django.contrib.auth.models import User

# Create your models here.
class ProductVariantAttribute(models.Model):
    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE
    )
    attribute = models.ForeignKey(
        Attribute,
        on_delete=models.PROTECT
    )
    attribute_value = models.ForeignKey(
        AttributeValue,
        on_delete=models.PROTECT
    )
    is_active = models.BooleanField(
        default=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='product_variant_attributes_created',
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='product_variant_attributes_updated',
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
        return self.product_variant.product.name + ' ' + self.attribute_value.value

    class Meta:
        verbose_name = 'Product Variant Attribute'
        verbose_name_plural = 'Product Variant Attributes'
        db_table = "product_variant_attribute"
        constraints = [
            models.UniqueConstraint(
                fields=['product_variant', 'attribute'],
                name='uq_product_variant_attribute_product_attribute_value'
            ),
        ]