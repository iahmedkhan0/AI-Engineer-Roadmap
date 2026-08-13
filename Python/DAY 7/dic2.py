marks = {
    "Math": 85,
    "Python": 92,
    "DBMS": 78,
    "OS": 88
}
highest = 0
highest_sub = ""
for subject, mark in marks.items():
    if mark>highest:
        highest = mark
        highest_sub = subject
print(highest_sub,highest)