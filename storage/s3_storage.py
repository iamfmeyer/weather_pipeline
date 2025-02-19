# src/storage/s3_storage.py

import boto3
import json
from datetime import datetime
from typing import Any, Dict, Optional
from botocore.exceptions import ClientError
import logging


class S3Storage:
    def __init__(self, bucket_name: str):
        self.s3_client = boto3.client("s3")
        self.bucket_name = bucket_name
        self._ensure_bucket_exists()

    def _ensure_bucket_exists(self):
        """Ensures the S3 bucket exists"""

        try:
            self.s3_client.head_bucket(Bucket=self.bucket_name)
        except ClientError:
            self.s3_client.create_bucket(
                Bucket=self.bucket_name,
                CreateBucketConfiguration={"LocationConstraint": "eu-central-1"},
            )

    def store_data(
        self,
        data: Dict[str, Any],
        dataset_type: str,
        metadata: Optional[Dict[str, Any]] = None,
        partition_keys: Optional[Dict[str, str]] = None,
    ) -> str:
        pass
