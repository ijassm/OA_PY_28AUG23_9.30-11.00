from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from constant import USERNAME, PASSWORD
from bson import ObjectId


uri = f"mongodb+srv://{USERNAME}:{PASSWORD}@oa.lybaz26.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["PY_DB"]

students = db["Students"]

# doc = {
#     "name": "xyz",
#     "age": 15,
#     "address": {
#         "doorNo": 10,
#         "street": "vengateshwara nagar",
#         "area": "saram",
#         "city": "puducherry",
#     },
#     "skills": ["PY", "JAVA"],
#     "phoneNumber": "+91 9876543210",
#     "createdAt": datetime.datetime.now(),
# }

###### create(adding single document)

# students.insert_one(doc)

###### create(adding multiple document)

# data = [
#     {
#         "name": "Alice",
#         "age": 25,
#         "address": {
#             "doorNo": 5,
#             "street": "Sunset Avenue",
#             "area": "Willowville",
#             "city": "Los Angeles",
#         },
#         "skills": ["C++", "Python"],
#         "phoneNumber": "+1 1234567890",
#         "createdAt": "2023-11-07T10:00:00",
#     },
#     {
#         "name": "Bob",
#         "age": 30,
#         "address": {
#             "doorNo": 15,
#             "street": "Maple Street",
#             "area": "Greenville",
#             "city": "New York",
#         },
#         "skills": ["JavaScript", "Ruby"],
#         "phoneNumber": "+1 2345678901",
#         "createdAt": "2023-11-07T11:30:00",
#     },
#     {
#         "name": "Eve",
#         "age": 28,
#         "address": {
#             "doorNo": 8,
#             "street": "Cedar Lane",
#             "area": "Pineville",
#             "city": "Chicago",
#         },
#         "skills": ["Java", "SQL"],
#         "phoneNumber": "+1 3456789012",
#         "createdAt": "2023-11-07T13:15:00",
#     },
#     {
#         "name": "Charlie",
#         "age": 22,
#         "address": {
#             "doorNo": 25,
#             "street": "Oakwood Road",
#             "area": "Birchville",
#             "city": "San Francisco",
#         },
#         "skills": ["C#", "PHP"],
#         "phoneNumber": "+1 4567890123",
#         "createdAt": "2023-11-07T14:45:00",
#     },
#     {
#         "name": "David",
#         "age": 35,
#         "address": {
#             "doorNo": 12,
#             "street": "Elm Street",
#             "area": "Hicksville",
#             "city": "Houston",
#         },
#         "skills": ["Ruby", "Perl"],
#         "phoneNumber": "+1 5678901234",
#         "createdAt": "2023-11-07T16:20:00",
#     },
# ]

# students.insert_many(data)

# read(finding one document)

# query = {"age": 25}

# unique id
# query = {"_id": ObjectId("6549cf208cf1361886fa3539")}


# getData = students.find_one(query)

# print(getData)

####### read(finding many documents)

# query = {"age": 25}

# getDatas = students.find(query)

# print(list(getDatas))

##### update data
# id = input("enter your id: ")


# try:
#     query = {"_id": ObjectId(id)}
#     age = int(input("enter your age to update: "))
#     update = {"$set": {"age": age}}
#     obj = students.update(query, update)
#     print("updated successfully", obj)
# except Exception as e:
#     # print(e)
#     print("id is invalid please try again")


# students.update_one(query)

#####update many

# query = {"age": 30}
# update = {"$set": {"age": 25}}


# students.update_many(query, update)

###### delete one

# query = {"_id": ObjectId("6549cd566d16cb17e7a03c34")}

# students.delete_one(query)

###### delete many
# query = {"age": 25}

# students.delete_many({})

# students.drop()
