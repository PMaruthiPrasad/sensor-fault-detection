import pymongo
import json
import pandas as pd

client=pymongo.MongoClient("mongodb+srv://maru:9490308421@cluster0.9epteuq.mongodb.net/")
#DATA_FILE_PATH="D:\D\Projects\Sensor Fault detection\sensor-fault-detection\aps_failure_training_set1.csv"
DATABASE='aps2'
COLLECTION_NAME='sensor2'


if __name__ == '__main__':
    df=pd.read_csv("aps_failure_training_set1.csv")
    #print(f"ROWS and columns: {df.shape}")

# Convert data from to Json s can dump these records in mongodb

    df.reset_index(drop=True,inplace=True)
    json_record=list(json.loads(df.T.to_json()).values())
    #print(json_record[0])


# Insert converted record to mongodb 
    client[DATABASE][COLLECTION_NAME].insert_many(json_record)

