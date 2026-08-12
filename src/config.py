from pathlib import Path
BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / "sample_data" / "orders.csv"
OUTPUT_DIR = BASE_DIR / "output"
CURATED_FILE = OUTPUT_DIR / "orders_curated.csv"
REJECTED_FILE = OUTPUT_DIR / "orders_rejected.csv"
