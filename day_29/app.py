from flask import Flask, Response,request,jsonify
import os
import json
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo
from datetime import datetime

app = Flask(__name__)

# select GET METhod
# URL for api  http://localhost:5000/api/v1.0/students
# dummy api data
"""
@app.route('/api/v1.0/students', methods = ['GET'])
def students ():
    student_list = [
        {
            'name':'Asabeneh',
            'country':'Finland',
            'city':'Helsinki',
            'skills':['HTML', 'CSS','JavaScript','Python']
        },
        {
            'name':'David',
            'country':'UK',
            'city':'London',
            'skills':['Python','MongoDB']
        },
        {
            'name':'John',
            'country':'Sweden',
            'city':'Stockholm',
            'skills':['Java','C#']
        }
    ]
    return Response(json.dumps(student_list), mimetype='application/json')
"""
MONGODB_URI = "mongodb+srv://UzairMasood:<password>@30daysofpython.zym1wu9.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python']

# get data from MongoDb using response
# select GET METhod
# URL for api  http://localhost:5000/api/v1.0/students
@app.route('/api/v1.0/students', methods = ['GET'])
def students ():
    student = db.student.find()
    return Response(dumps(student), mimetype='application/json')

# get data from MongoDb using response and id
# select GET METhod
# URL for api get data using id http://localhost:5000/api/v1.0/students/63be5ab74f0557cd52489c89
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.student.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')

# save data on mongodb
# go to postman select POST
# URL for this request http://localhost:5000/api/v1.0/students
# then select body and from body selcet raw
# then in click text menu and change into json
# write your json data and send requst
@app.route('/api/v1.0/students', methods = ['POST'])
def create_student ():
    name = request.json['name']
    country = request.json['country']
    city = request.json['city']
    skills = request.json['skills'].split(', ')
    birthyear = request.json['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'created_at': created_at
    }
    db.student.insert_one(student)
    return jsonify("data upload!")

# update user data
# go to postman select PUT
# URL for this request http://localhost:5000/api/v1.0/students/63be5ab74f0557cd52489c89
# then select body and from body selcet raw
# then in click text menu and change into json
# write your json data and send requst
@app.route('/api/v1.0/students/<id>', methods = ['PUT'])
def update_student (id):
    query = {"_id":ObjectId(id)}
    name = request.json['name']
    country = request.json['country']
    city = request.json['city']
    skills = request.json['skills'].split(', ')
    birthyear = request.json['birthyear']
    created_at = datetime.now()
    student = {
        '$set':{'name': name,
                'country': country,
                'city': city,
                'birthyear': birthyear,
                'skills': skills,
                'created_at': created_at
        }
    }
    db.student.update_one(query, student)
    return jsonify("user data update")

# Route for deleting data using id
# go to postman select DELETE
# URL for this request http://localhost:5000/api/v1.0/students/63be5ab74f0557cd52489c89
# then select body and from body selcet raw
# then in click text menu and change into json
# write your json data and send requst
@app.route('/api/v1.0/students/<id>', methods = ['DELETE'])
def delete_student (id):
    db.student.delete_one({"_id":ObjectId(id)})
    return jsonify("user deleted")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)