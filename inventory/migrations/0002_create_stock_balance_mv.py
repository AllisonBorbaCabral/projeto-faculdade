from django.db import migrations
from django.conf import settings
from pathlib import Path


def create_stock_balance_view(apps, schema_editor):
    engine = schema_editor.connection.vendor

    if engine == "postgresql":
        sql_path = Path(
            "inventory/queries/postgres/mv_stock_balance_create.sql"
        )
    elif engine == "sqlite":
        sql_path = Path(
            "inventory/queries/sqlite/v_stock_balance_create.sql"
        )
    else:
        return

    schema_editor.execute(sql_path.read_text())


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_stock_balance_view),
    ]