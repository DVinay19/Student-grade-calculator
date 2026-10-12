
print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

maths = int(input("Enter Maths marks (0-100): "))
science = int(input("Enter Science marks (0-100): "))
english = int(input("Enter English marks (0-100): "))
social = int(input("Enter Social marks (0-100): "))

# Validate marks
if not (0 <= maths <= 100 and
        0 <= science <= 100 and
        0 <= english <= 100 and
        0 <= social <= 100):
    print("Invalid marks! Each subject must be between 0 and 100.")

else:
    total = maths + science + english + social
    percentage = total / 400 * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    print("\n===== RESULT =====")
    print("Student:", name)
    print("Total:", total, "/ 400")
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
