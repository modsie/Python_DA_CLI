student_in_tupleclass = ('Sam', 'Matthaias', 'Bukola', 'Babatunde')

print(student_in_tupleclass[1])

for i in student_in_tupleclass:
    print(i)
    
    
student_in_setclass = {'Abeeb', 'Ibrahim', 'Babatunde', 'Bukola', 'Matthaias'}

print(student_in_setclass)

for i in student_in_setclass:
    print(i)
    
student1 = {
    'Name': 'Bukola',
    'Age': 16,
    'Location': 'Oyo',
    'Profession': 'Data Analyst',
    }
student2 = {
    'Name': 'Ibrahim',
    'Age': 35,
    'Location': 'Lagos',
    'Profession': 'Agba Baller',
    }
student3 = {
    'Name': 'Abbey',
    'Age': 20,
    'Location': 'Port Harcourt',
    'Profession': 'Agba Baller',
    }
student4 = {
    'Name': 'Babatunde',
    'Age': 35,
    'Location': 'Lagos',
    'Profession': 'Agba Baller',
    }
student5 = {
    'Name': 'Matthaias',
    'Age': 35,
    'Location': 'Lagos',
    'Profession': 'Agba Baller',
    }
print('')
print('')

x = 'Hello world' # strings
print(x)
print(x.upper())  # Indexing 
print(x.lower())

print(x[6:]) # indexing

p1 = 'Samuel'
p2 = 'Matthias'
p3 = 'Bukola'

list_of_students = ['Abeeb', 'Babatunde', 'Ibrahim', p1, p2, p3]
tuple_of_students = ('Abeeb', 'Babatunde', 'Ibrahim', 'Abeeb')
set_of_students = {'Abeeb', 'Babatunde', 'Ibrahim'}

print('\nlist')
for each_student in list_of_students:
    print(each_student)
list_of_students.append('Parach')
print(list_of_students)

print('\nTuple')
new_tuple_list = []
for each_student in tuple_of_students:
    print(each_student)
    new_tuple_list.append(each_student)

new_tuple_list.append('Parach')
tuple_of_students = tuple(new_tuple_list)
print(tuple_of_students, 'Tuple edited')

print('\nset')
for each_students in set_of_students:
    print(each_student)

# Dictionary
student1 = {
    'Name': 'Samuel',
    'Age': 45,
    'Profession': 'Software Engineer',
    'Location': 'Lagos',
    }

print(student1)
print(type(student1))
print(student1['Name'])

for each_key in student1:
    print(student1[each_key])

# Text - strings
# Number - Integer, Float, Complex
# Boolean - 
# Collection - List, Tuple, Set, Dictionary



# print(student1['Name'], student1['Age'], student1['Location'], student1['Profession'])
# print(student2['Name'], student2['Age'], student2['Location'], student2['Profession'])
# print(student3['Name'], student3['Age'], student3['Location'], student3['Profession'])
# print(student4['Name'], student4['Age'], student4['Location'], student4['Profession'])
# print(student5['Name'], student5['Age'], student5['Location'], student5['Profession'])

# print(student1)

# student1['Friends'] = ['Samuel', 'Matthaias', 'Abeeb']
# student1['Age'] = 65
# print(student1)

# for each_key in student1:
#     print(student1[each_key])
    
# student_list = [
#     student1, 
#     student2, 
#     student3, 
#     student4, 
#     student5
#     ]

# # print(student_list)

# # print('')
# # print('')
# # for each_student in student_list:
# #     print(each_student)
    
# # student6_name = input('Enter student name: ')
# # student6_age = input('Enter student age: ')
# # student6_location = input('Enter student location: ')
# # student6_profession = input('Enter student profession: ')

# # student6 = {
# #     'Name': student6_name,
# #     'Age': student6_age,
# #     'Location': student6_location,
# #     'Profession': student6_profession,
# #     }

