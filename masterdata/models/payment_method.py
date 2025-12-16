from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PaymentMethod(models.Model):
    name = models.CharField(
            max_length=255,
            null=False,
            blank=False,
        )
    is_active = models.BooleanField(
        default=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='payment_methods_created',
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='payment_methods_updated',
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
        verbose_name = 'Payment Method'
        verbose_name_plural = 'Payment Methods'
        constraints = [
            models.UniqueConstraint(
                fields=['name'],
                name='uq_payment_method_name'
            )
        ]