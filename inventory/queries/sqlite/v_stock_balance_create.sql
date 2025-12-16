CREATE VIEW v_stock_balance AS
SELECT
    smi.product_variant_id,
    sm.warehouse_id,
    SUM(
        CASE
            WHEN smt.direction = 'IN' THEN smi.quantity
            WHEN smt.direction = 'OUT' THEN -smi.quantity
            ELSE 0
        END
    ) AS quantity
FROM stock_movement_item smi
JOIN stock_movement sm ON sm.id = smi.movement_id
JOIN stock_movement_type smt ON smt.id = sm.movement_type_id
GROUP BY
    smi.product_variant_id,
    sm.warehouse_id;
