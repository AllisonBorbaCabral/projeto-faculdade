from django.db import models
from .attribute import Attribute
from django.contrib.auth.models import User

# Create your models here.
class AttributeValue(models.Model):
    value = models.CharField(
            max_length=100,
            null=False,
            blank=False,
        )
    attribute = models.ForeignKey(
        Attribute,
        on_delete=models.PROTECT,
        related_name='attribute_values',
    )
    is_active = models.BooleanField(
        default=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='attributevalues_created',
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='attributevalues_updated',
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

    def __str__(self):
        return f'{self.attribute.name}: {self.value}'

    class Meta:
        verbose_name = 'Attribute Value'
        verbose_name_plural = 'Attribute Values'
        constraints = [
            models.UniqueConstraint(
                fields=['value', 'attribute'],
                name='uq_attributevalue_value_attribute'
            )
        ]