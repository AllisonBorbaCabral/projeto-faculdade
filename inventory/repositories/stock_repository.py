from django.db import connection
from pathlib import Path
from inventory.models import StockMovement, StockMovementItem

SQL_DIR = Path(__file__).resolve().parent.parent / 'queries'

def load_sql(filename):
    return (SQL_DIR / filename).read_text()

def get_stock_balance(product_variant_id, warehouse_id):
    view_name = (
        "mv_stock_balance"
        if connection.vendor == "postgresql"
        else "v_stock_balance"
    )
    sql = f'''
        SELECT quantity
        FROM {view_name}
        WHERE product_variant_id = %s
        AND warehouse_id = %s
    '''
    
    with connection.cursor() as cursor:
        cursor.execute(sql, [product_variant_id, warehouse_id])
        row = cursor.fetchone()
        return row[0] if row else 0

def lock_stock_balance(product_variant_id, warehouse_id):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT 1
            FROM mv_stock_balance
            WHERE product_variant_id = %s
              AND warehouse_id = %s
            FOR UPDATE
            """,
            [product_variant_id, warehouse_id]
        )

def create_stock_movement(data):
    return StockMovement.objects.create(**data)


def create_stock_movement_item(data):
    return StockMovementItem.objects.create(**data)
