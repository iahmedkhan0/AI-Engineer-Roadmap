marks = {
    "Math": 85,
    "Python": 92,
    "DBMS": 78,
    "OS": 88
}
highest = 0
for mark in marks.values():
    if mark>highest:
        highest = mark
print(highest)