CREATE UNIQUE INDEX ux_mv_stock_balance
ON mv_stock_balance (product_variant_id, warehouse_id);

CREATE INDEX ix_mv_stock_balance_variant
ON mv_stock_balance (product_variant_id);