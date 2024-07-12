import sys
import os
import pymongo
import certifi

from us_visa_approval.exception import USvisaException
from us_visa_approval.logger import logging
from us_visa_approval.constants import DATABASE_NAME, CONNECTION_URL

ca = certifi.where()

class MongoDBClient:
    """_summary_
    Imports data from MongoDB as a dataframe
    """
    
    client = None
    
    def __init__(self, database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(CONNECTION_URL)
                if mongo_db_url is None:
                    raise Exception(f'Environment key {CONNECTION_URL} is not set')
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile = ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info('MongoDB connection successful')
        except Exception as e:
            raise USvisaException(e,sys)