import os
import sys
import sys
import json
import pymongo
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ce=certifi.where()

import pandas as pd
import numpy as np
from NetworkSecurity.logging.logger import logging
from NetworkSecurity.exception.exception import networkSecurityException
    

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise networkSecurityException(e,sys)

    def csv_to_json_converter(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)

            '''We will store our data into list of JSON in the mongo BD. '''
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise networkSecurityException(e,sys)
        
    def insert_data_to_mongodb(self,records,databse,collection):
        try:
            self.database=databse
            self.collection=collection
            self.records=records

            self.mongo_clint=pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_clint[self.database]
            
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise networkSecurityException(e,sys)     


if __name__=='__main__':
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="networkDb-Mayukh"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_converter(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_to_mongodb(records,DATABASE,Collection)
    print(no_of_records)           