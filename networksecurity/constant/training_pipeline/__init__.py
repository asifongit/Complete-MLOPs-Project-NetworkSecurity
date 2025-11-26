import os
import sys
import numpy as np
import pandas as pd


"""
defining common constant variables for training pipeline

"""
TARGET_COLUMN: str = "Result"
PIPELINE_NAME: str = "network_security_pipeline"
ARTIFACT_DIR: str = "Artifact"
FILE_NAME: str = "phisingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

SCHEMA_FILE_PATH: str = os.path.join("data_schema","schema.yaml")


"""
Data Ingestion related constant value starting with DATA_INGESTION_VAR_*
"""
DATA_INGESTION_COLLECTION_NAME: str = "Phising_Collection"
DATA_INGESTION_DATABASE_NAME: str = "Asif_Network_Security_DB"
DATA_INGESTION_DIR_NAME: str= "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_TRAIN_DIR: str = "train"
DATA_INGESTION_TEST_DIR: str = "test"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2




"""
Data Validation related constant value starting with DATA_VALIDATION_VAR_*

"""

DATA_VALIDATION_DIR_NAME: str= 'data_validation'
DATA_VALIDATION_VALID_DIR: str = 'validated'
DATA_VALIDATION_INVALID_DIR: str = 'invalid'
DATA_VALIDATION_DRIFT_REPORT_DIR: str = 'drift_report'
DATA_VALIDATION_DRIFT_FILE_NAME: str = 'report.yaml'