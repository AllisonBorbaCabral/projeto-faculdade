from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Unit(models.Model):
    name = models.CharField(
            max_length=255,
            null=False,
            blank=False,
        )
    symbol = models.CharField(
        max_length=10,
        null=False,
        blank=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='units_created',
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='units_updated',
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
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'symbol'],
                name='uq_unit_name_symbol'
            )
        ]