CREATE OR REPLACE FUNCTION fn_validate_stock_balance(
    p_product_variant_id INT,
    p_warehouse_id INT,
    p_quantity NUMERIC
)
RETURNS VOID AS $$
DECLARE
    v_balance NUMERIC;
BEGIN
    SELECT quantity
    INTO v_balance
    FROM mv_stock_balance
    WHERE product_variant_id = p_product_variant_id
      AND warehouse_id = p_warehouse_id
    FOR UPDATE;

    IF v_balance IS NULL OR v_balance < p_quantity THEN
        RAISE EXCEPTION 'Insufficient stock';
    END IF;
END;
$$ LANGUAGE plpgsql;