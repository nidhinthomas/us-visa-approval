import os
from datetime import date



# Defining Connection Variables for MongoDB Connection

DATABASE_NAME = 'US_VISA'
COLLECTION_NAME = 'VISA_DATA'
CONNECTION_URL = 'mongodb+srv://nidhinthomas:nidhinthomas@cluster0.lpwgvtf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

# Pipeline Variables

PIPELINE_NAME: str = 'usvisa'
ARTIFACT_DIR: str = 'artifacts'

MODEL_FILE_NAME = 'model.pkl'

TARGET_COLUMN = 'case_status'

CURRENT_YEAR = date.today().year

PREPROCESSING_OBJECT_FILE_NAME = 'preprocessing.pkl'

FILE_NAME = 'EasyVisa.csv'
TRAIN_FILE_NAME = 'train.csv'
TEST_FILE_NAME = 'test.csv'

# Data Ingestion variables

DI_COLLECTION_NAME = 'visa_data'
DI_DIR_NAME = 'data_ingestion'
DI_FEATURE_STORE_DIR = 'feature_store'
DI_INGESTED_DIR = 'ingested'
DI_TEST_RATIO = 0.2

