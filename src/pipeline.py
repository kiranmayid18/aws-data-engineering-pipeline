import csv
from src.config import INPUT_FILE, OUTPUT_DIR, CURATED_FILE, REJECTED_FILE
from src.data_quality import validate_order
from src.transform import transform_order

def run_pipeline(input_file=INPUT_FILE):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    valid, rejected, seen = [], [], set()

    with input_file.open("r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            errors = validate_order(row, seen)
            if errors:
                rejected.append({**row, "validation_errors": " | ".join(errors)})
            else:
                seen.add(row["order_id"].strip())
                valid.append(transform_order(row))

    if valid:
        with CURATED_FILE.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=valid[0].keys())
            w.writeheader(); w.writerows(valid)

    if rejected:
        with REJECTED_FILE.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=rejected[0].keys())
            w.writeheader(); w.writerows(rejected)

    print(f"Pipeline complete: {len(valid)} valid, {len(rejected)} rejected")
    return len(valid), len(rejected)

if __name__ == "__main__":
    run_pipeline()
