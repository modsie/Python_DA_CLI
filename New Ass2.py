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
try:
    score_input = input("Enter the student's score: ")
    score = int(score_input)
    grade = find_student_grade(score)
    print(f"The student's grade is: {grade}")
except ValueError:
    print("Please enter a valid integer for the score.")
