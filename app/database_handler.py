import sys
import pandas as pd
import json
import os
import pymongo
from pymongo import MongoClient

#coffee_db initalize mongodb database with 2 csv files for coffee machines and coffee pods and handle selecting products from database
class coffee_db:
    def __init__(self,c_database = "coffee",cp_path="coffee_pods.csv",cm_path="coffee_machines.csv" , cm_collection = "coffee_machines" , cp_collection = "coffee_pods"):
        self.client = MongoClient("localhost:27017")
        self.database = self.client[c_database]
        if self.database[cp_collection].count_documents({})==0:
            self._load_data(cp_collection,cp_path)
        if self.database[cm_collection].count_documents({})==0:
            self._load_data(cm_collection,cm_path)
    def _load_data(self,collection, file_name):
        current_path = os.path.dirname(__file__)
        data_path = os.path.join(current_path, file_name) 
        data = pd.read_csv(data_path)
        data_json = json.loads(data.to_json(orient='records'))
        self.database[collection].insert_many(data_json)

    def get_products(self,collection, filter):
        products = list(self.database[collection].find(filter).distinct("product_name"))
        return products






