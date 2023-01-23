from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.gj54vpd.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students = db.students
docs = db.students.find({})

print("-- DISPLAYING STUDENT DOCUMENTS FROM FIND() QUERY --")
for doc in docs:
    print(doc)

print("\n")

result = db.students.update_one({'student_id': '1007'}, {'$set': {'last_name': 'Anderson'}})

doc = db.students.find_one({"student_id": "1007"})
print(doc)