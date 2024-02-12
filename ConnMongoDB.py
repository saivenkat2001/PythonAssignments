import json
from bson import ObjectId

import pymongo

conn_str = "mongodb+srv://admin:admin@cluster0.zgbvu5e.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(conn_str)

myDB1 = client["pymango_demo1"]
# print(myDB1)
# print(client.list_database_names())

myCollection = myDB1["demo_collection1"]
#
# with open('config.json', 'r') as f:
#     data=json.load(f)
#
# res = myCollection.insert_many([data])
# print(res.inserted_ids)
# print(myCollection)
# print(myDB1)
# print(client.list_database_names())
#


#
# newCollection = myCollection.update_one({
#     "row1": {
#       "emp_id":101 ,
#       "emp_name": "raj",
# 	  "emp_gender":"M",
# 	  "emp_dept":"testing"
#     }},{"$set":{
#         "row1": {
#       "emp_id":101 ,
#       "emp_name": "raju",
# 	  "emp_gender":"Male",
# 	  "emp_dept":"testing"
#
# }}})
#
# print(newCollection)
for i in myCollection.find():
    print(i)


record = myCollection.delete_one({'_id': ObjectId('65c5efafdf994c7cdce6d563')})
print(record)