from pymongo import MongoClient
import pandas
import json
import dicttoxml
# import os

# Building a new client instance of MongoClient

mongo_client = MongoClient('localhost', 27017)
# Here, Database name = company
db = mongo_client.company
# collection = PROJECTS 
collection = db.PROJECTS 

# Making API call to the MongoDB Server

cursor = collection.find()
mongo_docs = list(cursor)

# Create the empty Dataframe
documents = pandas.DataFrame(columns=[])

for doc in mongo_docs:
    doc["_id"] = str(doc["_id"])
    doc_id = doc["_id"]
    # Cteating the Series object from the dictionary in MongoDB
    series_obj = pandas.Series( doc, name=doc_id )
    documents = documents.append(series_obj)

# Remove the object-Id as it is not needed 
documents = documents.drop(columns=['_id'])

# Convert the documents dataframe to json, orient to go record wise
json_file = documents.to_json(orient='records')
# Using json.loads to desearialize the json file. i.e convert the string into object 
obj = json.loads(json_file)
# Using dicttoxml to convert the JSON Object to XML
xml = dicttoxml.dicttoxml(obj, attr_type = False)
f = open("PROJECTS.xml","wb")
f.write(xml)
f.close


