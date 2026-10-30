import json  # import the json module to work with JSON data
subjects = ("Mathematics", "English", "Computer Science") # a tuple that contains the subjects
data_file_valid = True

def add_student():
    if not data_file_valid:  # to not allow adding student data if the data file is corrupted
        print("Cannot add student because the data file is corrupted.")
        return
    valid_name=False
    while not valid_name:       
        name = input("Enter student name: ").strip()
        if not name:  # check if the name is empty
            print("Error: Name cannot be empty. Please enter a valid name.")
        else:
            valid_name=True  # set valid_name to True to exit the loop
    check=False  # a boolean variable to check if the roll number is valid
    while not check:
        try:
            roll_no = int(input("Enter student roll number: "))  # input the roll number and convert it to an integer
            if any(student["roll_no"] == roll_no for student in students):  # check if the roll number already exists in the students list
                print("Error: Roll number already exists. Please enter a unique roll number.")
                check = False  # set check to False to continue the loop
            elif roll_no <= 0:  # check if the roll number is a positive integer
                print("Error: Roll number must be a positive integer.")
                check = False  # set check to False to continue the loop
            else:
                check = True  # set check to True to exit the loop
        except ValueError:
            print("Error: Invalid roll number. Please enter a valid integer.")
            
    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": {}
    }
    for subject in subjects:
        print(subject)
        valid_marks = False
        while not valid_marks:
            try:
                # Take marks input
                input_marks = int(input(f"Enter marks for {subject}: "))  # input marks for each subject 
                # Validate marks range
                if not 0 <= input_marks <= 100:
                    print("Error: Marks must be between 0 and 100.")
                    valid_marks = False
                else:
                    valid_marks = True
                    student["marks"][subject] = input_marks  # append the marks to the student dictionary

            except ValueError:
                # Display an appropriate error message
                print("Error: Invalid marks. Please enter a valid integer.")
    students.append(student)  # appends adds the student dictionary to the students list       
        
    if data_file_valid:
        save_students_to_file()   # to save the studenst data in file 
        print("Student added successfully!")
        
    else:
        print("Failed to add student. Please check the data file.")
        return
    
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
    if data_file_valid:
        with open("students.json", 'w') as file:
                json.dump(students, file, indent=4)  # save the students list to a JSON file with indentation for readability
    else:
        # Display a message that saving is blocked
        print("Saving is blocked due to file validation issues.")
    




def load_students_from_file():
    global data_file_valid
    try:
        with open("students.json", 'r') as file:
            return json.load(file)  # load the students list from a JSON file
    except FileNotFoundError:
        return []  # if the file does not exist, return an empty list
    except json.JSONDecodeError:
    # Display an error message
        print("Error: Failed to decode JSON from the file. Starting with an empty student list.")
        data_file_valid = False  # set the data_file_valid flag to False
        return []     # Return an empty list
    
students = load_students_from_file()

print("STUDENT PERFORMANCE ANALYZER")
print("-----------------------------")

print("Available Subjects:", subjects)
add_student()  # call the function to add a student
#print("Student Records:", students)  # print the student records to the terminal
