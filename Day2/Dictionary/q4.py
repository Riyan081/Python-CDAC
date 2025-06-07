stud = {
    'Arham': 'Blue',
    'Lisa': 'Yellow',
    'Vinod': 'Purple',
    'Jenny': 'Pink'
}

print("Student Details:" ,stud)

# 1. Find number of students
print("Total students:", len(stud))

# 2. Change Lisa’s favourite colour
stud['Lisa'] = 'Green'

# 3. Remove 'Jenny' and her favourite color
del stud['Jenny']

# 4. Sort and print students and their favourite colours alphabetically by name
for name in sorted(stud):
    print(name, ":", stud[name])