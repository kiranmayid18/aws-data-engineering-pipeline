# Architecture Notes

This design uses Amazon S3 as durable raw/curated storage, SQS to decouple ingestion from processing, and SNS for operational alerts.

For larger workloads, Python workers can run on Lambda, ECS, or EC2 Auto Scaling. VPC controls can isolate compute and warehouse resources. EBS can provide persistent block storage for EC2 workloads, while ELB is relevant when ingestion is exposed as a service/API.

Key production considerations:
- idempotent processing;
- dead-letter queues;
- data freshness and volume monitoring;
- partitioning and lifecycle rules;
- least-privilege IAM;
- CI/CD promotion across environments;
- CloudWatch metrics and alarms.
