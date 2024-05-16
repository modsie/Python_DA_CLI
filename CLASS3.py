# Python Collection/Array
# Loop a list

Student_list = ['Ibrahim', 'Matthias', 'Bukola', 'Babatunde', 'Abeeb']
age_list = [21, 13, 46, 7]

print('Hello, good morning', Student_list[0])
print('Hello, good morning', Student_list[1])
print('Hello, good morning', Student_list[2])
print('Hello, good morning', Student_list[3])
print('Hello, good morning', Student_list[4])

# For loop
# Iteration

#for each_student in Student_list:
    # print(each_student)
    #pos = Student_list.index(each_student)
    #print(pos, 'Hello, good morning', each_student)
    #print('')
    
    #pos = Student_list.index(each_student)
    #print(pos+1, 'Hello, good morning', each_student)
    #print('')

for each_student in Student_list:
    pos = Student_list.index(each_student)
    print(f'{pos+1} Hello, good morning {each_student}')
    print('')

# Python collections
    




