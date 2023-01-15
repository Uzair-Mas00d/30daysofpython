from flask import Flask, render_template
import os
import pymongo
from bson.objectid import ObjectId

#db = client.name_of_databse 
#db = client['name_of_database'] # Two ways of creating database in Mongodb
MONGODB_URI = "mongodb+srv://UzairMasood:<password>@30daysofpython.zym1wu9.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(MONGODB_URI)
db = client.thirty_days_of_python

# inserting data using insert_one()
"""db.student.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
print(client.list_database_names())
"""
"""
students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
for student in students:
    db.student.insert_one(student)
"""
# Find collection using find_one()
"""
students = db.student.find_one()

students = db.student.find_one({"_id":ObjectId('63be4d9d8fd946281eca5afe')})
print(students)
"""
#Find collection using find()
"""
students = db.student.find()
students = db.student.find({}, {"_id":0,  "name": 1, "country":1})

query = {
    "country":"Finland"
} 
query = {
    "city":"Helsinki"
}
query = {
    "country":"Finland",
    "city":"Helsinki"
}
query = {"age":{"$gt":30}}
query = {"age":{"$lt":30}}
students = db.student.find(query)

students = db.student.find().limit(3)
for student in students:
    print(student)
"""
# Sort by name
"""
Accesnding order
students = db.student.find().sort('name') 
for student in students:
    print(student)

Deccesnding order
students = db.student.find().sort('name',-1)
for student in students:
    print(student)
"""
# sort by age
"""
Accesnding order
students = db.students.find().sort('age') 
for student in students:
    print(student)

Deccesnding order
students = db.student.find().sort('age',-1)
for student in students:
    print(student)
"""
# Update value using update_one()
"""
query = {'age':210}
new_value = {'$set':{'age':38}}
db.student.update_one(query, new_value)

for student in db.student.find():
    print(student)
"""
# delete using delete_one() 
"""
query = {'name':'John'}
db.student.delete_one(query)

for student in db.student.find():
    print(student)
"""
# for deleting whole collection
"db.student.drop()"

app = Flask(__name__)

if __name__ == "main":
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True,host="0.0.0.0",port=port)