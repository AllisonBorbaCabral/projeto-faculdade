from django.db import transaction
from django.core.exceptions import ValidationError

from inventory.repositories.stock_repository import (
    get_stock_balance,
    lock_stock_balance,
    create_stock_movement,
    create_stock_movement_item
)

@transaction.atomic
def create_stock_out(
    *,
    movement_type,
    warehouse,
    items,
    reference=None,
    movement_date=None,
    notes=None
):
    """
    items = [
        {
            "product_variant": obj,
            "quantity": Decimal,
            "unit_cost": Decimal | None
        }
    ]
    """

    movement = create_stock_movement({
        "movement_type": movement_type,
        "warehouse": warehouse,
        "reference": reference,
        "movement_date": movement_date,
        "notes": notes
    })

    for item in items:
        product_variant = item["product_variant"]
        quantity = item["quantity"]

        lock_stock_balance(product_variant.id, warehouse.id)

        available = get_stock_balance(
            product_variant.id,
            warehouse.id
        )

        if available < quantity:
            raise ValidationError(
                f"Insufficient stock for {product_variant}. "
                f"Available: {available}"
            )

        create_stock_movement_item({
            "movement": movement,
            "product_variant": product_variant,
            "quantity": quantity,
            "unit_cost": item.get("unit_cost")
        })

    return movement

@transaction.atomic
def create_stock_in(
    *,
    movement_type,
    warehouse,
    items,
    reference=None,
    movement_date=None,
    notes=None
):
    movement = create_stock_movement({
        "movement_type": movement_type,
        "warehouse": warehouse,
        "reference": reference,
        "movement_date": movement_date,
        "notes": notes
    })

    for item in items:
        create_stock_movement_item({
            "movement": movement,
            "product_variant": item["product_variant"],
            "quantity": item["quantity"],
            "unit_cost": item.get("unit_cost")
        })

    return movement

@transaction.atomic
def create_stock_transfer(
    *,
    movement_type_out,
    movement_type_in,
    warehouse_from,
    warehouse_to,
    items,
    reference=None,
    movement_date=None
):
    # Saída
    create_stock_out(
        movement_type=movement_type_out,
        warehouse=warehouse_from,
        items=items,
        reference=reference,
        movement_date=movement_date,
        notes="Transfer OUT"
    )

    # Entrada
    create_stock_in(
        movement_type=movement_type_in,
        warehouse=warehouse_to,
        items=items,
        reference=reference,
        movement_date=movement_date,
        notes="Transfer IN"
    )