students = {
    "student1": {
        "name": "Ahmed",
        "age": 20
    },
    "student2": {
        "name": "Ali",
        "age": 21
    }
}
for student in students.values():
    print(student["name"],student["age"])