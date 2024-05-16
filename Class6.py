# Create a list of number value
# Write s function that adds all the numbers in the list together


student_list = []
Student1 = {
    'Name': 'Bukola',
    'Location': 'Ibadan',
    'Age': '16',
    'Profession': 'Programmer',
    'friends': ['Matthias', 'Babatunde']
}

Student2 = {
    'Name': 'Matthias',
    'Location': 'Lagos',
    'Age': '47',
    'Profession': 'Technologist',
    'friends': ['Matthias', 'Ibrahim']
}

Student3 = {
    'Name': 'Ibrahim',
    'Location': 'Oyo',
    'Age': '49',
    'Profession': 'Business',
    'friends': ['Samuel', 'Babatunde']
}

Student4 = {
    'Name': 'Babatunde',
    'Location': 'Abuja',
    'Age': '28',
    'Profession': 'Doctor',
    'friends': ['Matthias', 'Bukola']
}

# Write a function that adds the age of all students together

python_student_list = [
    Student1, 
    Student2, 
    Student3, 
    Student4, 
    ]

def addStudentsAge(all_students): # Parameter/requirements

    # result =0
    # for each_student in all_students:
    #     print(each_student['Age'])
    #     result += int(each_student['Age'])

    # print(result)

    age_list = []
    for each_student in all_students:
        age_list.append(int(each_student['Age']))

    print(sum(age_list))

addStudentsAge(python_student_list) # Argument

# Agrs (Argument)
# Default Argument

def showProfile(Name, Age, Location='Parach', *friends):
    
    print(f"""
        The name of the student - {Name}.
        Student is {Age} years old.
        Student is currently in {Location}
        """)# f'' Format - to pass a variable into a string
    
    for friend in friends:
        print(f'{Name} has a friend called {friend}')

showProfile(
        Student1['Name'],
        Student1['Age'],
        Student1['Location'],
        Student1['friends']
)

'''
Create a list of atleast 5 states and capital from user option 1 - 4
Perform: 
1. Read- display all states and capital 
2. Create - User can add a state and capital
3. Update - User can edit a particular state and capital 
4. Delete - User can delete a particular state and capital
'''

def sh(Name, location= 'Parach'):

    print(f'Student name is {Name}, student lives at {location}')

    sh('Bukola', 'Lagos')
    sh('Matthias', 'Ibadan')
