from us_visa_approval.configuration.mongo_db_connection import MongoDBClient
from us_visa_approval.constants import DATABASE_NAME
from us_visa_approval.exception import USvisaException
from typing import Optional

import pandas as pd
import numpy as np
import sys

class USVisaData:
    def __init__(self):
        try:
            self.mongodb_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise USvisaException(e, sys)
    
    def convert_collection_to_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            if database_name is None:
                collection = self.mongodb_client.database[collection_name]
            else:
                collection = self.mongodb_client[database_name][collection_name]
            
            df = pd.DataFrame(list(collection.find()))
            if '_id' in df.columns:
                df = df.drop(columns = ['_id'])
            df.replace({'na': np.nan}, inplace=True)
            return df
        except Exception as e:
            raise USvisaException(e, sys)

