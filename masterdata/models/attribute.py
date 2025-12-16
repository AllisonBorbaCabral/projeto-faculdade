from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Attribute(models.Model):
    name = models.CharField(
            max_length=100,
            null=False,
            blank=False,
        )
    is_active = models.BooleanField(
        default=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='attributes_created',
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='attributes_updated',
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
        verbose_name = 'Attribute'
        verbose_name_plural = 'Attributes'
        db_table='attribute'
        constraints = [
            models.UniqueConstraint(
                fields=['name'],
                name='uq_attribute_name'
            )
        ]