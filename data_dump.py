import pymongo
import pandas as pd
import json
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"

DATABASE_NAME='aps'
COLLECTION_NAME='sensor'



if __name__=="__main__":

     df=pd.read_csv(DATA_FILE_PATH)
     print(f"rows and coliumns:{df.shape}")  

## convert datafarme into json format

df.reset_index(drop=True,inplace=True)

json_record=list(json.loads(df.T.to_json()).values())  ## df convert into json list
print(json_record[0])  ## print some json records

## inserted convert json into mango db

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


    




