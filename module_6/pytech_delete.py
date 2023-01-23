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

gerry = {
"student_id": "1010", 
"first_name": "Gerry", 
"last_name": "Doe"
}

gerry_student_id = students.insert_one(gerry).inserted_id
print("-- INSERT STATEMENTS --")
print("Inserted student record John Morris into the students collection with document id " + str(gerry_student_id))

doc = db.students.find_one({"student_id": "1010"})

print("\n")

print("-- DISPLAYING STUDENT TEST DOC --")
print(doc)

delete = db.students.delete_one({"student_id": "1010"})

print("\n")

new_doc = db.students.find({})
print("-- DISPLAYING STUDENT DOCUMENTS FROM FIND() QUERY --")
for new in new_doc:
    print(new)

