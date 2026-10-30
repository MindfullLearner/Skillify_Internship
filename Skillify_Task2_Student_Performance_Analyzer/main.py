import json  # import the json module to work with JSON data
subjects = ("Mathematics", "English", "Computer Science") # a tuple that contains the subjects

students = []  # a  list to store the grades

def add_student():
    name = input("Enter student name: ")
    roll_no = int(input("Enter student roll number: "))
    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": {}
    }
    for subject in subjects:
        print(subject)
        input_marks = int(input(f"Enter marks for {subject}: "))  # input marks for each subject 
        student["marks"][subject] = input_marks  # append the marks to the student dictionary
    
    students.append(student)  # appends adds the student dictionary to the students list

    print("Student added successfully!")
    save_students_to_file()   # to save the studenst dat in file 
    print("========== STUDENT SUMMARY ==========")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_no}")
    print("\nSubject-wise Marks:")
    for subject, marks in student["marks"].items():
        print(f"{subject}: {marks}")
    print("\nTotal Marks:", sum(student["marks"].values()))  # calculate the total marks and print it
    average_marks= calculate_average(student["marks"])  # call the function to calculate the average marks
    print(f"Average: {average_marks:.2f}")
    print(f"Grade: {calculate_grade(average_marks)}")  # call the function to calculate the grade and print it
    print(f"Performance: {get_performance_level(average_marks)}")  # call the function to calculate the performance level and print it
    print("\n=======================================")

def calculate_average(marks):
    total_marks = sum(marks.values())  # sum of all the marks
    average = total_marks / len(marks)  # calculate the average marks
    return average

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def get_performance_level(average):
    if average >= 90:
        return "Excellent"
    elif average >= 80:
        return "Very Good"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Average"
    elif average >= 50:
        return "Below Average"
    else:
        return "Poor"

def save_students_to_file():
    with open("students.json", 'w') as file:
        json.dump(students, file, indent=4)  # save the students list to a JSON file with indentation for readability
#dictionary that contains the student records like name,rollno,marks etc
print("STUDENT PERFORMANCE ANALYZER")
print("-----------------------------")

print("Available Subjects:", subjects)
add_student()  # call the function to add a student
#print("Student Records:", students)  # print the student records to the terminal
