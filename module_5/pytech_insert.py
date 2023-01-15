from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.gj54vpd.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students = db.students

john = {
"student_id": "1007", 
"name": "John", 
"last name": "Morris"
}
thomas = {
"student_id": "1008", 
"first name": "Thomas", 
"last_name": "Smith", 
}
dave = {
"student_id": "1009", 
"first name": "Dave", 
"last name": "Rice" 
}

john_student_id = students.insert_one(john).inserted_id
thomas_student_id = students.insert_one(thomas).inserted_id
dave_student_id = students.insert_one(dave).inserted_id

print("-- INSERT STATMENTS --")
print("Inserted student record John Morris into the students collection with document id " + str(john_student_id))
print("Inserted student record Thomas Smith into the students collection with document id " + str(thomas_student_id))
print("Inserted student record Dave Rice into the students collection with document id " + str(dave_student_id))


