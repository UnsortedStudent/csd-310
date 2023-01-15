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

print(john_student_id)
print(thomas_student_id)
print(dave_student_id)


