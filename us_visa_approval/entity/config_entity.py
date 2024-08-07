import os
from us_visa_approval.constants import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime('%m_%d_%Y_%H_%M_%S')

@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
    timestamp: str = TIMESTAMP

training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DI_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DI_FEATURE_STORE_DIR, FILE_NAME)
    training_file_path: str = os.path.file(data_ingestion_dir, DI_INGESTED_DIR, TRAIN_FILE_NAME)
    testing_file_path: str = os.path.file(data_ingestion_dir, DI_INGESTED_DIR, TEST_FILE_NAME)
    train_test_split_ratio: float = DI_TEST_RATIO
    COLLECTION_NAME: str = DI_COLLECTION_NAME