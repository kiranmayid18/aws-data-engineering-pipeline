# AWS Data Engineering Pipeline

Portfolio/demo project showing AWS-oriented data engineering using Python, SQL, ETL/ELT, data quality and CI/CD.

> This is a portfolio project, not a production client system.

## Architecture

Source CSV/JSON -> Amazon S3 -> S3 Event -> Amazon SQS -> Python Transformation -> Curated S3 -> SQL Warehouse  
Failures / quality thresholds -> Amazon SNS alerts

## Skills demonstrated
- AWS: S3, SQS, SNS, EC2, VPC, EBS, ELB, Auto Scaling concepts
- Python ETL
- SQL and star-schema data warehousing
- Data quality and validation
- Git + GitHub Actions CI/CD
- Scalable, decoupled pipeline design

## Business scenario
Daily e-commerce order files arrive from multiple channels. The pipeline validates, standardises and prepares them for analytics while separating rejected records.

## Run locally
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
python -m src.pipeline
pytest -q
```

## Repository structure
```text
.github/workflows/ci.yml
src/
sql/
tests/
sample_data/
docs/
README.md
```

## Data model
A star schema with:
- dim_customer
- dim_product
- dim_date
- fact_order

## Production AWS mapping
- Raw/curated/rejected zones: Amazon S3
- Event buffering: Amazon SQS
- Alerts: Amazon SNS
- Processing: Lambda, ECS, or EC2 Auto Scaling
- Networking: VPC/private subnets/security groups
- Persistent EC2 storage: EBS
- Service load balancing: ELB
- Monitoring: CloudWatch
- Analytical warehouse: Redshift or another SQL warehouse

## Author
Kiranmayi Dodda  
GitHub: https://github.com/kiranmayid18
