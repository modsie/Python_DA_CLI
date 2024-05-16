student_grade = A1 = 75 - 100
B2 = 70 - 74
B3 = 65 - 69
C4 = 60 - 64
C5 = 55 - 59
C6 = 50 - 54
D7 = 45 - 49
E8 = 40 - 44
F9 = 0 - 39


score = 80

grading_scale = {
    'A1': range(75, 101),
    'B2': range(70, 75),
    'B3': range(65, 70),
    'C4': range(60, 65),
    'C5': range(55, 60),
    'C6': range(50, 55),
    'D7': range(45, 50),
    'E8': range(40, 45),
    'F9': range(0, 40)
}

student_grade = None
for grade, score_range in grading_scale.items():
    if score in score_range:
        student_grade = grade
        break

print(f"The student grade for a score of {score} is: {student_grade}")

def find_student_grade(score):
    if 75 <= score <= 100:
        return 'A1'
    elif 70 <= score <= 74:
        return 'B2'
    elif 65 <= score <= 69:
        return 'B3'
    elif 60 <= score <= 64:
        return 'C4'
    elif 55 <= score <= 59:
        return 'C5'
    elif 50 <= score <= 54:
        return 'C6'
    elif 45 <= score <= 49:
        return 'D7'
    elif 40 <= score <= 44:
        return 'E8'
    elif 0 <= score <= 39:
        return 'F9'
    else:
        return 'Invalid score'

# Get score from user input
score = int(input("Enter the student's score: "))

# Find the student's grade
grade = find_student_grade(score)
print(f"The student's grade is: {grade}")
