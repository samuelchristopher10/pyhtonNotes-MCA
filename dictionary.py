student = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science",
}

student["age"] = 21
print(student["age"])
student.update({"major": "Data Science", "name": "samuel"})
print(student)
print(student.pop("name"))
print(student)
student.popitem()
print(student)
print(student.update({"year": 2024}))
print(student)

i = {
    "name": ["farooq","samuel","veer the robo boy"],
    "type": ["student","student","robot"],
    "age": [20, 21, 22],
}

for key in i.keys():
    print(key)
    print(i[key])
for key, value in i.items():
    print(key, value)