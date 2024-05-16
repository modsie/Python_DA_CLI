student = 'Samuel'
student2 = 'Ibadan'
student3 = 'Parach'
student4 = 'Ibrahim'

student_list = [student, student2, student3, student4]


print(student_list[ 0:2])


# revisionClass.py

print("Hello world")

x = "anything"


# Variable are container that holds data/value

num1 = 2
num2  = 5
# I
result = num1 * num2
print(result)

result = num1 / num2
print(result)

result = num1 + num2
print(result)

result = num1 - num2
print(result)

result = 'Samuel'
print(result)

# Data Type
# Datatype determines operation

# Arithmetic Operation - Integer 
# Data type
# Float, String, Boolean, Complex, Dictionary, Tuple, Set, List

'''
Data Type
String
Integer : Integer, Float(decimal), Complex(2e7)
Boolean
Collection/Array : List, Tuple, Set, Dictionary

Identify
String - ""
Interger - Number
Boolean - True/False
List - [] # Square bracket
set - {} # Curly bracket
Tuple - () # Curv bracket
Dictionary - { Key:Value } # comes in pairs of key and value
'''


student = 'Samuel'
student2 = 'Ibadan'
student3 = 'Parach'
student4 = 'Ibrahim'

student_list = [student, student3, student2, student4]

print(student_list[1:3])

list_item2 = student_list[1]
print(list_item2[:2].upper())

# print(student_list[1][:2].upper())
# Hello Samuel, welcome to class, pay up

for each_student in student_list:
    # print(each_student)
    
    # if student2 == each_student:
    if "Ibadan" == each_student:
        print(f'Hello {each_student}, welcome to class, pay up')
    else:
        print(f'Hello {each_student}, welcome to class')
    
    
'''
Create a list of at least 5 states and capital.
From user option 1-4
1. Read - display all stats and capital
2. Create - User can add a state and it capital
3. Update - User can edit a particular state and capital
4. Delete - User can delete a particular state and capital
'''
    
state1 = { 'State': 'Oyo', 'Capital': 'Ibadan'}
state2 = { 'State': 'Lagos', 'Capital': 'Ikeja'}
state3 = { 'State': 'Ogun', 'Capital': 'Abeokuta'}
state4 = { 'State': 'Osun', 'Capital': 'Osogbo'}
state5 = { 'State': 'Ekiti', 'Capital': 'Ado-Ekiti'}

stateCapital_list = [state1, state2, state3, state4, state5]

def stateCapital():
    print('''
    Enter 1 to view list of states and capital
    Enter 2 to add a state and capital
    Enter 3 to edit a state of you choice
    Enter 4 to delete a particular state and it capital
    ''')
    
    user_input = input('Enter your option: ')
    
    if user_input == '1':
        print('View list of states and capital')
    elif user_input == '2':
        print('Add a state and capital')
    elif user_input == '3':
        print('Edit a state of you choice')
    elif user_input == '4':
        print('Delete a particular state and it capital')
    else:
        print('Input invalid')
        
        
stateCapital()