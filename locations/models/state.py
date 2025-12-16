from django.db import models
from datetime import datetime
from .country import Country
from django.contrib.auth.models import User

# Create your models here.
class State(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    acronym = models.CharField(
        max_length=3,
        null=False,
        blank=False,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        related_name='states',
        db_column='country_id',
    )
    is_active = models.BooleanField(
        default=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='states_created',
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='states_updated',
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
        verbose_name = 'State'
        verbose_name_plural = 'States'
        db_table='state'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'acronym'],
                name='uq_state_name_acronym'
            )
        ]