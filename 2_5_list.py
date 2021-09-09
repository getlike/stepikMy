students = ['one', 'two','jopa']
print('len list = ' , len(students))

for student in students:
    print("stud " + student + "!")

students.append('aded')
print(students[-1])
students+='omg'
print("--------------------------------")
students.insert(1, 'inserted')


for student in students:
    print("stud " + student + "!")
