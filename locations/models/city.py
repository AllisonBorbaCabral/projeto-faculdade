from django.db import models
from datetime import datetime
from .state import State
from django.contrib.auth.models import User

# Create your models here.
class City(models.Model):
    name = models.CharField(
            max_length=255,
            null=False,
            blank=False,
        )
    area_code = models.CharField(
        max_length=4,
        null=False,
        blank=False,
    )
    state = models.ForeignKey(
        State,
        on_delete=models.PROTECT,
        related_name='cities',
    )
    is_active = models.BooleanField(
        default=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='cities_created',
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='cities_updated',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
    )
    updated_at = models.DateTimeField(     
        auto_now=True,   
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'state'],
                name='uq_city_name_state'
            )
        ]