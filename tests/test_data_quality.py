from src.data_quality import validate_order

def row():
    return {
        "order_id":"O1","order_date":"2026-08-01","customer_id":"C1",
        "customer_name":"Alice","product_id":"P1","product_name":"Keyboard",
        "quantity":"1","unit_price":"10","source_system":"WEB"
    }

def test_valid():
    assert validate_order(row(), set()) == []

def test_duplicate():
    assert "duplicate order_id" in validate_order(row(), {"O1"})

def test_bad_quantity():
    r = row(); r["quantity"] = "0"
    assert "quantity must be greater than zero" in validate_order(r, set())
