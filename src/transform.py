from datetime import datetime

def transform_order(row):
    order_date = datetime.strptime(row["order_date"].strip(), "%Y-%m-%d").date()
    quantity = int(row["quantity"])
    unit_price = float(row["unit_price"])
    return {
        "order_id": row["order_id"].strip(),
        "order_date": order_date.isoformat(),
        "customer_id": row["customer_id"].strip(),
        "customer_name": row["customer_name"].strip().title(),
        "product_id": row["product_id"].strip(),
        "product_name": row["product_name"].strip().title(),
        "quantity": quantity,
        "unit_price": round(unit_price, 2),
        "sales_amount": round(quantity * unit_price, 2),
        "source_system": row["source_system"].strip().upper(),
    }
