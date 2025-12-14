from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Country(models.Model):
    name = models.CharField(
            max_length=255,
            null=False,
            blank=False,
        )
    idd = models.CharField(
        max_length=4,
        null=False,
        blank=False,
    )
    acronym = models.CharField(
        max_length=3,
        null=False,
        blank=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='countries_created',
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='countries_updated',
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
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'acronym'],
                name='uq_country_name_acronym'
            )
        ]