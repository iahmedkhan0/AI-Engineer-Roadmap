students = {
    "student1": {
        "name": "Ahmed",
        "marks": 85
    },
    "student2": {
        "name": "Ali",
        "marks": 92
    },
    "student3": {
        "name": "Sara",
        "marks": 78
    }
}
highest = 0
highest_student = ""
for student in students.values():
    if student["marks"] > highest:
        highest = student["marks"]
        highest_student = student["name"]
print(highest_student, highest)