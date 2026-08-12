from src.transform import transform_order

def test_sales_amount():
    row = {
        "order_id":"O1","order_date":"2026-08-01","customer_id":"C1",
        "customer_name":"alice smith","product_id":"P1","product_name":"keyboard",
        "quantity":"2","unit_price":"25.50","source_system":"web"
    }
    result = transform_order(row)
    assert result["sales_amount"] == 51.0
    assert result["customer_name"] == "Alice Smith"
    assert result["source_system"] == "WEB"
