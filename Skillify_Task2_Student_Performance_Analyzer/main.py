subjects = ("Mathematics", "English", "Computer Science") # a tuple that contains the subjects

students = []  # a  list to store the grades

def add_student():
    name = input("Enter student name: ")
    roll_no = int(input("Enter student roll number: "))
    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": []
    }
    students.append(student)  # appends adds the student dictionary to the students list
    print("Student added successfully!")



#dictionary that contains the student records like name,rollno,marks etc
print("STUDENT PERFORMANCE ANALYZER")
print("-----------------------------")

print("Available Subjects:", subjects)
add_student()  # call the function to add a student
print("Student Records:", students)  # print the student records to the terminal
