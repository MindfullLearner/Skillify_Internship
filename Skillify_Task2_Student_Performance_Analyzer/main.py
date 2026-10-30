import json  # import the json module to work with JSON data
subjects = ("Mathematics", "English", "Computer Science") # a tuple that contains the subjects
data_file_valid = True

def add_student():
    if not data_file_valid:  # to not allow adding student data if the data file is corrupted
        print("Cannot add student because the data file is corrupted.")
        return
    print("\n========== ADD STUDENT ===============")
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
        print("==================END=====================")
        display_student_summary(student)
    else:
        print("Failed to add student. Please check the data file.")
        print("==================END=====================")
        return
    
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

def display_all_students():
    if not students:
        print("No student records found.")
        return

    print("\n========== ALL STUDENT RECORDS =========")
    for student in students:
        print("-" * 40)
        print(f"Name: {student['name']}")
        print(f"Roll Number: {student['roll_no']}")
        print("Subject-wise Marks:")
        for subject, marks in student["marks"].items():
            print(f"{subject}: {marks}")
        average = calculate_average(student["marks"])
        print(f"Average: {average:.2f}")
        print(f"Grade: {calculate_grade(average)}")

    print("================END========================")

def display_student_summary(student):
    print("========== STUDENT SUMMARY ==========")
    # Display name
    print(f"Name: {student['name']}")
    # Display roll number
    print(f"Roll Number: {student['roll_no']}")
    # Display subject-wise marks
    print("Subject-wise Marks:")
    for subject, marks in student["marks"].items():
        print(f"{subject}: {marks}")
    # Calculate and display total
    total = sum(student["marks"].values())
    print(f"Total: {total}")
    # Calculate and display average
    average = calculate_average(student["marks"])
    print(f"Average: {average:.2f}")
    # Display grade
    print(f"Grade: {calculate_grade(average)}")
    # Display performance
    print(f"Performance: {get_performance_level(average)}")
    print("\n===============END=====================")

def show_menu():   
    print("======STUDENT PERFORMANCE ANALYZER=======")
    is_running=True
    while is_running:
        print("Menu: ")
        print("1. Add Student")
        print("2. Display all Students Record")
        print("3. Exit")
        try:
            option=int(input("Enter the option: "))
            if option<0:
                print("Invalid Option. Please Try again.")
                continue
            if option==1:
                print("Available Subjects:", subjects)
                add_student()
            elif option==2:
                display_all_students()
            elif option==3:
                is_running=False
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Error: Invalid option. Please enter a valid integer option.")
students = load_students_from_file()

#main
show_menu()

