from datetime import datetime

REQUIRED_FIELDS = {
    "order_id","order_date","customer_id","customer_name",
    "product_id","product_name","quantity","unit_price","source_system"
}

def validate_order(row, seen_order_ids):
    errors = []
    missing = sorted(f for f in REQUIRED_FIELDS if not str(row.get(f, "")).strip())
    if missing:
        errors.append("missing required fields: " + ", ".join(missing))

    order_id = str(row.get("order_id", "")).strip()
    if order_id and order_id in seen_order_ids:
        errors.append("duplicate order_id")

    try:
        if int(row.get("quantity", 0)) <= 0:
            errors.append("quantity must be greater than zero")
    except (TypeError, ValueError):
        errors.append("quantity must be an integer")

    try:
        if float(row.get("unit_price", -1)) < 0:
            errors.append("unit_price must be zero or greater")
    except (TypeError, ValueError):
        errors.append("unit_price must be numeric")

    try:
        datetime.strptime(str(row.get("order_date", "")), "%Y-%m-%d")
    except ValueError:
        errors.append("order_date must use YYYY-MM-DD")

    return errors
