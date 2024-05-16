#students_list
students_list = student1 = {
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
# Extract ages of students and find the mean from the students_list?

students_list = [student1, student2, student3, student4, student5]
Age = []
for student in students_list:
    Age.append(student['Age'])

mean_age = sum(Age) / len(Age)

print("Students Age:", Age)
print("Mean of Students Age:", mean_age)

