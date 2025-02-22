# Initialize an empty dictionary for student grades
student_grades = {}

# Specify the number of subjects to collect
num_subjects = int(input("How many subjects would you like to enter grades for? "))

# Use a for loop to collect user inputs
for i in range(num_subjects):
    subject = input(f"Enter the subject name for subject {i + 1}: ")
    grade = input(f"Enter the grade for {subject}: ")

    # If the subject already exists, append the grade to the list
    if subject in student_grades:
        student_grades[subject].append(grade)
    else:
        # Create a new list if the subject doesn't exist
        student_grades[subject] = [grade]

# Display the collected data
print("Student Grades:")
for subject, grades in student_grades.items():
    print(f"{subject}: {grades}")