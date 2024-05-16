
def studentProfile():
    name = input('Enter your name: ')
    age = input('Enter your age: ')

    print(f'Student name is {name}, student is {age} years old')

    # studentProfile()

    def personProfile(name, age, location):
        print(f'Student name is {name}')
        print(f'student is {age} years old')
        print(f'student lives at {location}')

        # personProfile('Bukola', 16, 'Ibadan')
        # personProfile('Samuel', 87, 'Lagos')


        ###############################
        '''
        OOP Object  Oriented Programming
        Python Class/Object

        Human Being
        Attribute,name, age, gender, hair_color, height, weight, profession...
        Method/Action - running, eating, sing..
        if weight is 80 - 100
        running speed = 20kph
        if weight is 60 - 80
        running speed = 40kph
        if weight is 40 - 60
        running speed = 50kph


        Car
        Attribute - color, name, model, type, speed, manufacturer, manufacturing-date
        Action - car_type, honk,

        school
        Attribute - name, location, students, teachers,
        Method - teach
        '''

class Car():

    def __init__(self, name, model, max_speed, color, manufacturer):
        self.name = name
        self.model = model
        self.max_speed = max_speed
        self.color = color
        self.manufacturer = manufacturer

    def car_type(self):
        '''
        speed < 100 = normal car
        speed (100 - 150 ) = modern car
        speed (151 - 200 ) = exotic car
        speed (200 - 250 ) = muscle car
        speed (250 - 300 ) = sport car
        speed >= 301 = super car
         '''
        if self.max_speed >= 301:
            print(f'The {self.name.capitalize()} car is a supar car')
        elif self.max_speed >= 250:
            print(f'The {self.name.capitalize()} car is a sport car')
        elif self.max_speed >= 200:
            print(f'The {self.name.capitalize()} car is a muscle car')
        elif self.max_speed >= 151:
            print(f'The {self.name.capitalize()} car is a exotic car')
        elif self.max_speed >= 100:
            print(f'The {self.name.capitalize()} car is a modern car')
        else:
            print(f'The {self.name.capitalize()} car is a normal car')



Car1 = Car(
    name = 'Toyota',
    model = 'Camry',
    max_speed = 200,
    color = 'Burgundy greenish yellow',
    manufacturer = ''
    )

Car2 = Car( 
    name = 'Honda',
    model = 'Civic',
    max_speed = 80,
    color = 'Burgundy greenish yellow',
    manufacturer = ''
    )
print(Car1.model)
print(Car2.name)
print(Car2.car_type())
print(Car2.color)
# studentFile = open('student_list.txt', 'r')

# print(studentFile)

import student_list
from student_list import students

print(students)

    




