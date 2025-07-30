import os
import sys
import numpy as np
import pandas as pd
import pymongo
from typing import List
from sklearn.model_selection import train_test_split

from NetworkSecurity.exception.exception import networkSecurityException
from NetworkSecurity.logging.logger import logging
from NetworkSecurity.entity.config_entity import DataIngestionConfig

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")

class DataIngestion():
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config

        except Exception as e:
            raise networkSecurityException(e,sys)
        
    def export_collection_as_dataframe(self):

        '''
        Read the data from mongodb
        '''
        try:
            database_name= self.data_ingestion_config.database_name
            collection_name=self.data_ingestion_config.collection_name
            self.mongo_clint=pymongo.MongoClient(MONGO_DB_URL)
            collection=self.mongo_clint[database_name][collection_name]

            df=pd.DataFrame(list(collection.find()))
            if "_id" in df.columns:
                df=df.drop("_id",axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df

        except Exception as e:
            raise networkSecurityException(e,sys)

    def export_data_to_festure_store(self,dataframe: pd.DataFrame):
        try:
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            #creating the folder
            dir_path=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True) 
            dataframe.to_csv(feature_store_file_path,index=False,header=True)

        except Exception as e:
            raise networkSecurityException(e,sys)
        
    def Initiate_data_ingestion(self):
        try:
            dataframe=self.export_collection_as_dataframe( )
            dataframe=self.export_collection_as_dataframe(dataframe)

        except Exception as e:
            raise networkSecurityException(e,sys)    
    

## to be continued