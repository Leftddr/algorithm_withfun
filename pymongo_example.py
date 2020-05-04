from pymongo import MongoClient
import datetime
import json
import pandas as pd
import numpy as np
import csv

client = MongoClient('localhost', 27017)
db = client['test1']
collection = db['test_collection']

df = pd.read_csv('/home/kernel/Desktop/fake_job_postings.csv')
df_columns = df.columns

df_dummies = pd.get_dummies(df['required_education'])
print(df_dummies.head())

df_for_dict = {}

arr = [1, 2, 3]
if 1 in arr:
    print("ok")

for col_name in df_columns:
    df_for_dict[col_name] = ""
'''
for i in range(0, len(df)):
    df_for_dict = {}
    for col_name in df_columns:
        df_for_dict[col_name] = str(df.iloc[i][col_name]) + str(1)
    collection.insert(df_for_dict)
'''
#print(collection.count_documents({}))
print(collection.find_one({"required_education" : "Bachelor's Degree1"}))


